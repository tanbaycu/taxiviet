from flask import Flask, request, render_template, redirect, url_for, flash, jsonify, send_file
from flask_mail import Mail, Message
import os
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__, static_folder="static", template_folder=".")
app.secret_key = os.urandom(24)  # For flash messages

app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # Change based on your email provider
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'testuserbaycu@gmail.com'  # Replace with admin email
app.config['MAIL_PASSWORD'] = 'jqzq kbqh hywd gmxw'  # Replace with app password
app.config['MAIL_DEFAULT_SENDER'] = ('Tuấn Taxi Website', 'tanbaycu@gmail.com')
app.config['ADMIN_EMAIL'] = 'tranquoctuan19861986@gmail.com'  # Replace with admin email

mail = Mail(app)

@app.route('/')
def index():
    return send_file('index.html')

@app.route('/submit_booking', methods=['POST'])
def submit_booking():
    """Handle booking form submission"""
    try:
        # Log all form data for debugging
        logger.info(f"Received booking form data: {request.form}")
        
        # Extract form data using the name attributes from the HTML
        fullname = request.form.get('fullname', 'Không có tên')
        phone = request.form.get('phone', 'Không có SĐT')
        email = request.form.get('email', 'Không cung cấp')
        pickup_address = request.form.get('pickup-address', 'Không có điểm đón')
        destination_address = request.form.get('destination-address', 'Không có điểm đến')
        booking_date = request.form.get('booking-date', 'Không có ngày')
        booking_time = request.form.get('booking-time', 'Không có giờ')
        car_type = request.form.get('car-type', 'Không chọn loại xe')
        notes = request.form.get('notes', 'Không có ghi chú')
        
        # Log the booking
        logger.info(f"New booking from {fullname} ({phone})")
        
        # Format the email content
        email_subject = f"Đặt Xe Mới: {fullname} - {booking_date} {booking_time}"
        email_body = f"""
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
            <li><strong>Điểm đón:</strong> {pickup_address}</li>
            <li><strong>Điểm đến:</strong> {destination_address}</li>
            <li><strong>Ngày đi:</strong> {booking_date}</li>
            <li><strong>Giờ đón:</strong> {booking_time}</li>
            <li><strong>Loại xe:</strong> {car_type}</li>
        </ul>
        
        <h3>Ghi chú:</h3>
        <p>{notes}</p>
        """
        
        # Send email to admin
        msg = Message(
            subject=email_subject,
            recipients=[app.config['ADMIN_EMAIL']],
            html=email_body
        )
        mail.send(msg)
        
        # Return success response
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return jsonify({"success": True, "message": "Cảm ơn bạn đã đặt xe! Chúng tôi sẽ liên hệ với bạn trong thời gian sớm nhất."})
        else:
            flash("Cảm ơn bạn đã đặt xe! Chúng tôi sẽ liên hệ với bạn trong thời gian sớm nhất.")
            return redirect(url_for('index', _anchor='booking'))
            
    except Exception as e:
        logger.error(f"Error processing booking: {str(e)}")
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return jsonify({"success": False, "message": "Có lỗi xảy ra. Vui lòng thử lại sau hoặc gọi trực tiếp cho chúng tôi."})
        else:
            flash("Có lỗi xảy ra. Vui lòng thử lại sau hoặc gọi trực tiếp cho chúng tôi.")
            return redirect(url_for('index', _anchor='booking'))

@app.route('/submit_contact', methods=['POST'])
def submit_contact():
    """Handle contact form submission"""
    try:
        # Log all form data for debugging
        logger.info(f"Received contact form data: {request.form}")
        
        # Extract form data using the name attributes from the HTML
        name = request.form.get('contact-name', 'Không có tên')
        email = request.form.get('contact-email', 'Không có email')
        phone = request.form.get('contact-phone', 'Không có SĐT')
        subject = request.form.get('contact-subject', 'Không có chủ đề')
        message = request.form.get('contact-message', 'Không có tin nhắn')
        
        # Log the contact
        logger.info(f"New contact from {name} ({email})")
        
        # Format the email content
        email_subject = f"Liên Hệ Mới: {name} - {subject}"
        email_body = f"""
        <h2>Thông Tin Liên Hệ Mới</h2>
        <p><strong>Thời gian gửi:</strong> {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}</p>
        
        <h3>Thông Tin Người Gửi:</h3>
        <ul>
            <li><strong>Họ và tên:</strong> {name}</li>
            <li><strong>Email:</strong> {email}</li>
            <li><strong>Số điện thoại:</strong> {phone}</li>
            <li><strong>Chủ đề:</strong> {subject}</li>
        </ul>
        
        <h3>Nội Dung Tin Nhắn:</h3>
        <p>{message}</p>
        """
        
        # Send email to admin
        msg = Message(
            subject=email_subject,
            recipients=[app.config['ADMIN_EMAIL']],
            html=email_body
        )
        mail.send(msg)
        
        # Return success response
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return jsonify({"success": True, "message": "Cảm ơn bạn đã gửi tin nhắn! Chúng tôi sẽ phản hồi trong thời gian sớm nhất."})
        else:
            flash("Cảm ơn bạn đã gửi tin nhắn! Chúng tôi sẽ phản hồi trong thời gian sớm nhất.")
            return redirect(url_for('index', _anchor='contact'))
            
    except Exception as e:
        logger.error(f"Error processing contact: {str(e)}")
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return jsonify({"success": False, "message": "Có lỗi xảy ra. Vui lòng thử lại sau hoặc gọi trực tiếp cho chúng tôi."})
        else:
            flash("Có lỗi xảy ra. Vui lòng thử lại sau hoặc gọi trực tiếp cho chúng tôi.")
            return redirect(url_for('index', _anchor='contact'))

@app.route('/quick_booking', methods=['POST'])
def quick_booking():
    """Handle quick booking form submission"""
    try:
        # Log all form data for debugging
        logger.info(f"Received quick booking form data: {request.form}")
        
        # Extract form data using the name attributes from the HTML
        pickup = request.form.get('pickup', 'Không có điểm đón')
        destination = request.form.get('destination', 'Không có điểm đến')
        date = request.form.get('date', 'Không có ngày')
        time = request.form.get('time', 'Không có giờ')
        
        # Log the quick booking
        logger.info(f"New quick booking from {pickup} to {destination}")
        
        # Format the email content
        email_subject = f"Đặt Xe Nhanh: {date} {time}"
        email_body = f"""
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
        
        # Send email to admin
        msg = Message(
            subject=email_subject,
            recipients=[app.config['ADMIN_EMAIL']],
            html=email_body
        )
        mail.send(msg)
        
        # Return success response
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return jsonify({"success": True, "message": "Cảm ơn bạn đã đặt xe! Chúng tôi sẽ liên hệ với bạn trong thời gian sớm nhất."})
        else:
            flash("Cảm ơn bạn đã đặt xe! Chúng tôi sẽ liên hệ với bạn trong thời gian sớm nhất.")
            return redirect(url_for('index'))
            
    except Exception as e:
        logger.error(f"Error processing quick booking: {str(e)}")
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return jsonify({"success": False, "message": "Có lỗi xảy ra. Vui lòng thử lại sau hoặc gọi trực tiếp cho chúng tôi."})
        else:
            flash("Có lỗi xảy ra. Vui lòng thử lại sau hoặc gọi trực tiếp cho chúng tôi.")
            return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)