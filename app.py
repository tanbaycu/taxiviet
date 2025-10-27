from flask import Flask, request, render_template, redirect, url_for, flash, jsonify
from flask_mail import Mail, Message
import os
from datetime import datetime
import logging
from user_agents import parse as parse_ua
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__, static_folder="app/static", template_folder="app/templates")
app.secret_key = os.urandom(24)

# Mail configuration
app.config.update(
    MAIL_SERVER=os.getenv("MAIL_SERVER"),
    MAIL_PORT=int(os.getenv("MAIL_PORT", 587)),
    MAIL_USE_TLS=os.getenv("MAIL_USE_TLS", "True") == "True",
    MAIL_USERNAME=os.getenv("MAIL_USERNAME"),
    MAIL_PASSWORD=os.getenv("MAIL_PASSWORD"),
    MAIL_DEFAULT_SENDER=os.getenv("MAIL_DEFAULT_SENDER"),
    ADMIN_EMAIL=os.getenv("ADMIN_EMAIL")
)

mail = Mail(app)

# Constants
MESSAGES = {
    "success_booking": "Cảm ơn bạn đã đặt xe! Chúng tôi sẽ liên hệ với bạn trong thời gian sớm nhất.",
    "success_contact": "Cảm ơn bạn đã gửi tin nhắn! Chúng tôi sẽ phản hồi trong thời gian sớm nhất.",
    "error": "Có lỗi xảy ra. Vui lòng thử lại sau hoặc gọi trực tiếp cho chúng tôi."
}

DEFAULT_VALUES = {
    "fullname": "Không có tên",
    "phone": "Không có SĐT",
    "email": "Không cung cấp",
    "pickup": "Không có điểm đón",
    "destination": "Không có điểm đến",
    "date": "Không có ngày",
    "time": "Không có giờ",
    "car_type": "Không chọn loại xe",
    "notes": "Không có ghi chú",
    "subject": "Không có chủ đề",
    "message": "Không có tin nhắn"
}


def _should_use_mobile_template(user_agent_string: str) -> bool:
    """Check if mobile template should be used"""
    user_agent = parse_ua(user_agent_string or "")
    return bool(user_agent.is_mobile or user_agent.is_tablet)


def _send_email(subject: str, body: str) -> None:
    """Send email to admin"""
    admin_email = app.config.get("ADMIN_EMAIL")
    if not admin_email:
        logger.error("ADMIN_EMAIL not configured")
        return
    msg = Message(subject=subject, recipients=[admin_email], html=body)
    mail.send(msg)


def _handle_response(success: bool, message: str, anchor: str | None = None):
    """Handle both AJAX and regular form responses"""
    if request.headers.get("X-Requested-With") == "XMLHttpRequest":
        return jsonify({"success": success, "message": message})
    
    if success:
        flash(message)
    
    # Fix: Only pass _anchor if it's not None
    if anchor:
        return redirect(url_for("index", _anchor=anchor))
    return redirect(url_for("index"))


def _get_form_value(key: str, default_key: str | None = None) -> str:
    """Get form value with default fallback"""
    # Fix: Use default_key if provided, otherwise use key
    fallback_key = default_key if default_key is not None else key
    return request.form.get(key, DEFAULT_VALUES.get(fallback_key, ""))


@app.route("/")
def index():
    """Redirect to appropriate template based on device"""
    use_mobile = _should_use_mobile_template(request.headers.get("User-Agent", ""))
    return redirect(url_for("mobile_html" if use_mobile else "index_html"))


@app.route("/index.html")
def index_html():
    return render_template("index.html")


@app.route("/mobile.html")
def mobile_html():
    return render_template("mobile.html")


@app.route("/submit_booking", methods=["POST"])
def submit_booking():
    """Handle booking form submission"""
    try:
        logger.info(f"Received booking form data: {request.form}")

        # Extract form data
        fullname = _get_form_value("fullname")
        phone = _get_form_value("phone")
        email = _get_form_value("email")
        pickup = _get_form_value("pickup-address", "pickup")
        destination = _get_form_value("destination-address", "destination")
        date = _get_form_value("booking-date", "date")
        time = _get_form_value("booking-time", "time")
        car_type = _get_form_value("car-type")
        notes = _get_form_value("notes")

        logger.info(f"New booking from {fullname} ({phone})")

        # Send email
        subject = f"Đặt Xe Mới: {fullname} - {date} {time}"
        body = f"""
        <h2>Thông Tin Đặt Xe Mới</h2>
        <p><strong>Thời gian đặt:</strong> {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}</p>
        
        <h3>Thông Tin Khách Hàng:</h3>
        <ul>
            <li><strong>Họ và tên:</strong> {fullname}</li>
            <li><strong>Số điện thoại:</strong> {phone}</li>
            <li><strong>Email:</strong> {email}</li>
        </ul>
        
        <h3>Thông Tin Chuyến Đi:</h3>
        <ul>
            <li><strong>Điểm đón:</strong> {pickup}</li>
            <li><strong>Điểm đến:</strong> {destination}</li>
            <li><strong>Ngày đi:</strong> {date}</li>
            <li><strong>Giờ đón:</strong> {time}</li>
            <li><strong>Loại xe:</strong> {car_type}</li>
        </ul>
        
        <h3>Ghi chú:</h3>
        <p>{notes}</p>
        """
        _send_email(subject, body)

        return _handle_response(True, MESSAGES["success_booking"], "booking")

    except Exception as e:
        logger.error(f"Error processing booking: {str(e)}")
        return _handle_response(False, MESSAGES["error"], "booking")


@app.route("/submit_contact", methods=["POST"])
def submit_contact():
    """Handle contact form submission"""
    try:
        logger.info(f"Received contact form data: {request.form}")

        # Extract form data
        name = _get_form_value("contact-name", "fullname")
        email = _get_form_value("contact-email", "email")
        phone = _get_form_value("contact-phone", "phone")
        subject_text = _get_form_value("contact-subject", "subject")
        message_text = _get_form_value("contact-message", "message")

        logger.info(f"New contact from {name} ({email})")

        # Send email
        subject = f"Liên Hệ Mới: {name} - {subject_text}"
        body = f"""
        <h2>Thông Tin Liên Hệ Mới</h2>
        <p><strong>Thời gian gửi:</strong> {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}</p>
        
        <h3>Thông Tin Người Gửi:</h3>
        <ul>
            <li><strong>Họ và tên:</strong> {name}</li>
            <li><strong>Email:</strong> {email}</li>
            <li><strong>Số điện thoại:</strong> {phone}</li>
            <li><strong>Chủ đề:</strong> {subject_text}</li>
        </ul>
        
        <h3>Nội Dung Tin Nhắn:</h3>
        <p>{message_text}</p>
        """
        _send_email(subject, body)

        return _handle_response(True, MESSAGES["success_contact"], "contact")

    except Exception as e:
        logger.error(f"Error processing contact: {str(e)}")
        return _handle_response(False, MESSAGES["error"], "contact")


@app.route("/quick_booking", methods=["POST"])
def quick_booking():
    """Handle quick booking form submission"""
    try:
        logger.info(f"Received quick booking form data: {request.form}")

        # Extract form data
        pickup = _get_form_value("pickup")
        destination = _get_form_value("destination")
        date = _get_form_value("date")
        time = _get_form_value("time")

        logger.info(f"New quick booking from {pickup} to {destination}")

        # Send email
        subject = f"Đặt Xe Nhanh: {date} {time}"
        body = f"""
        <h2>Thông Tin Đặt Xe Nhanh</h2>
        <p><strong>Thời gian đặt:</strong> {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}</p>
        
        <h3>Thông Tin Chuyến Đi:</h3>
        <ul>
            <li><strong>Điểm đón:</strong> {pickup}</li>
            <li><strong>Điểm đến:</strong> {destination}</li>
            <li><strong>Ngày đi:</strong> {date}</li>
            <li><strong>Giờ đón:</strong> {time}</li>
        </ul>
        
        <p><strong>Lưu ý:</strong> Đây là đặt xe nhanh từ form trên trang chủ. Cần liên hệ lại với khách hàng để xác nhận thông tin chi tiết.</p>
        """
        _send_email(subject, body)

        return _handle_response(True, MESSAGES["success_booking"])

    except Exception as e:
        logger.error(f"Error processing quick booking: {str(e)}")
        return _handle_response(False, MESSAGES["error"])


if __name__ == "__main__":
    app.run(debug=True, port=5000)