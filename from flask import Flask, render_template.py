from flask import Flask, render_template_string

app = Flask(__name__)

html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SHLOK ENTERPRISE</title>

    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: Arial, sans-serif;
            background: #f4f7fc;
            color: #222;
        }

        header {
            background: #071b3a;
            color: white;
            padding: 25px 15px;
            text-align: center;
        }

        header h1 {
            color: #f5c542;
            font-size: 35px;
        }

        nav {
            background: #102d59;
            padding: 15px;
            text-align: center;
        }

        nav a {
            color: white;
            text-decoration: none;
            margin: 12px;
            font-weight: bold;
        }

        .hero {
            background: linear-gradient(120deg, #071b3a, #1764a5);
            color: white;
            text-align: center;
            padding: 85px 20px;
        }

        .hero h2 {
            font-size: 38px;
            margin-bottom: 15px;
        }

        .hero p {
            font-size: 18px;
            line-height: 1.7;
        }

        .btn {
            display: inline-block;
            background: #f5c542;
            color: #071b3a;
            padding: 13px 25px;
            margin-top: 25px;
            border-radius: 6px;
            text-decoration: none;
            font-weight: bold;
        }

        section {
            padding: 55px 20px;
            text-align: center;
        }

        section h2 {
            color: #102d59;
            margin-bottom: 25px;
            font-size: 30px;
        }

        .services {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 20px;
        }

        .service {
            background: white;
            width: 280px;
            padding: 25px;
            border-radius: 12px;
            box-shadow: 0 3px 12px #0002;
        }

        .service h3 {
            color: #1764a5;
            margin-bottom: 12px;
        }

        .about p, .contact p {
            font-size: 17px;
            line-height: 1.8;
            max-width: 750px;
            margin: auto;
        }

        footer {
            background: #071b3a;
            color: white;
            padding: 20px;
            text-align: center;
        }

        @media(max-width: 600px) {
            header h1 {
                font-size: 27px;
            }

            .hero h2 {
                font-size: 28px;
            }

            nav a {
                display: inline-block;
                margin: 8px;
            }
        }
    </style>
</head>

<body>

<header>
    <h1>SHLOK ENTERPRISE</h1>
    <p>Your Digital Growth Partner | आपका डिजिटल विकास साथी</p>
</header>

<nav>
    <a href="#home">Home</a>
    <a href="#about">About</a>
    <a href="#services">Services</a>
    <a href="#contact">Contact</a>
</nav>

<div class="hero" id="home">
    <h2>Grow Your Business Digitally</h2>
    <p>
        हम आपके बिजनेस को डिजिटल दुनिया में आगे बढ़ाने में मदद करते हैं।
        <br>
        Creative Design | Digital Marketing | Website Development
    </p>
    <a class="btn" href="https://wa.me/919026542364">
        Contact on WhatsApp
    </a>
</div>

<section class="about" id="about">
    <h2>About Us | हमारे बारे में</h2>
    <p>
        SHLOK ENTERPRISE में आपका स्वागत है।
        हम Graphic Design, Digital Marketing, Website Development
        और Online Business Promotion की सेवाएँ प्रदान करते हैं।
        हमारा उद्देश्य आपके बिजनेस को ऑनलाइन पहचान दिलाना है।
    </p>
</section>

<section id="services">
    <h2>Our Services | हमारी सेवाएँ</h2>

    <div class="services">

        <div class="service">
            <h3>Graphic Design</h3>
            <p>Professional Poster, Banner, Logo और Brochure Design.</p>
        </div>

        <div class="service">
            <h3>Digital Marketing</h3>
            <p>Online Promotion और Business Marketing Services.</p>
        </div>

        <div class="service">
            <h3>Website Development</h3>
            <p>Professional और Responsive Website Development.</p>
        </div>

        <div class="service">
            <h3>SEO Services</h3>
            <p>Search Engine Optimization और Local SEO.</p>
        </div>

        <div class="service">
            <h3>Social Media Management</h3>
            <p>Facebook, Instagram और YouTube Management.</p>
        </div>

        <div class="service">
            <h3>Content Creation</h3>
            <p>Social Media Posts, Videos और Promotional Content.</p>
        </div>

    </div>
</section>

<section class="contact" id="contact">
    <h2>Contact Us | संपर्क करें</h2>
    <p>
        SHLOK ENTERPRISE
        <br>
        Mobile: 9026542364
        <br>
        अपने बिजनेस को डिजिटल बनाइए।
    </p>

    <a class="btn" href="tel:9026542364">Call Now</a>
    <a class="btn" href="https://wa.me/919026542364">
        WhatsApp
    </a>
</section>

<footer>
    <p>© 2026 SHLOK ENTERPRISE | All Rights Reserved</p>
</footer>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(html)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
    