from flask import Flask, render_template_string

app = Flask(__name__)

PAGE = r'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="Shlok Enterprise - your trusted business partner.">
  <title>Shlok Enterprise | Official Website</title>
  <style>
    :root {
      --navy: #101d36;
      --blue: #0879bd;
      --gold: #ffc107;
      --light: #f4f6fa;
      --white: #ffffff;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    html { scroll-behavior: smooth; }
    body {
      font-family: Arial, Helvetica, sans-serif;
      line-height: 1.6;
      color: #222;
      background: var(--light);
    }
    header {
      background: var(--navy);
      color: var(--white);
      padding: 18px 7%;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 16px;
      flex-wrap: wrap;
    }
    .logo { color: var(--gold); font-size: 25px; font-weight: 800; }
    nav { display: flex; flex-wrap: wrap; gap: 18px; }
    nav a { color: var(--white); text-decoration: none; font-weight: 700; }
    nav a:hover { color: var(--gold); }
    .hero {
      min-height: 440px;
      padding: 70px 20px;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      text-align: center;
      color: var(--white);
      background: linear-gradient(120deg, var(--navy), var(--blue));
    }
    .hero h1 { font-size: clamp(32px, 6vw, 52px); margin-bottom: 12px; }
    .hero p { font-size: 18px; margin: 5px 0; }
    .actions { margin-top: 22px; }
    .button {
      display: inline-block;
      margin: 5px;
      padding: 12px 22px;
      border-radius: 6px;
      background: var(--gold);
      color: var(--navy);
      text-decoration: none;
      font-weight: 700;
    }
    .button:hover { background: var(--white); }
    section { padding: 60px 8%; text-align: center; }
    .section-title { color: var(--navy); font-size: 32px; margin-bottom: 18px; }
    .about p { max-width: 760px; margin: 0 auto; }
    .services { background: #eaf0f8; }
    .service-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(210px, 1fr));
      gap: 20px;
      margin-top: 30px;
    }
    .service-card {
      background: var(--white);
      padding: 25px 20px;
      border-radius: 12px;
      box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);
    }
    .service-card h3 { color: var(--blue); margin-bottom: 10px; }
    .contact { background: var(--navy); color: var(--white); }
    .contact .section-title { color: var(--gold); }
    .contact p { margin: 9px 0; }
    .contact a:not(.button) { color: var(--gold); }
    footer { background: #081225; color: var(--white); text-align: center; padding: 20px; }
    .whatsapp {
      position: fixed;
      right: 18px;
      bottom: 18px;
      background: #25d366;
      color: var(--white);
      padding: 12px 18px;
      border-radius: 28px;
      text-decoration: none;
      font-weight: 700;
      box-shadow: 0 3px 12px rgba(0, 0, 0, 0.2);
    }
    @media (max-width: 600px) {
      header { justify-content: center; text-align: center; }
      nav { justify-content: center; gap: 12px; }
      section { padding: 45px 6%; }
    }
  </style>
</head>
<body>
  <header>
    <div class="logo">SHLOK ENTERPRISE</div>
    <nav aria-label="Main navigation">
      <a href="#home">Home</a>
      <a href="#about">About</a>
      <a href="#services">Services</a>
      <a href="#contact">Contact</a>
    </nav>
  </header>

  <main>
    <section class="hero" id="home">
      <h1>Welcome to Shlok Enterprise</h1>
      <p>Your Trusted Business Partner</p>
      <p>Quality • Reliability • Customer Satisfaction</p>
      <div class="actions">
        <a class="button" href="#services">Our Services</a>
        <a class="button" href="tel:+919026542364">Call Now</a>
      </div>
    </section>

    <section class="about" id="about">
      <h2 class="section-title">About Shlok Enterprise</h2>
      <p>
        Welcome to Shlok Enterprise. We believe in quality, reliability and
        customer satisfaction. Contact us to learn more about our business
        and the products or services we offer.
      </p>
    </section>

    <section class="services" id="services">
      <h2 class="section-title">Our Services</h2>
      <p>We are committed to dependable service and customer support.</p>
      <div class="service-grid">
        <article class="service-card">
          <h3>Quality Products</h3>
          <p>Quality-focused products and business solutions.</p>
        </article>
        <article class="service-card">
          <h3>Business Support</h3>
          <p>Helpful support for customers and business partners.</p>
        </article>
        <article class="service-card">
          <h3>Customer Service</h3>
          <p>Clear communication and a focus on customer satisfaction.</p>
        </article>
        <article class="service-card">
          <h3>Trusted Partnership</h3>
          <p>Building reliable, long-term business relationships.</p>
        </article>
      </div>
    </section>

    <section class="contact" id="contact">
      <h2 class="section-title">Contact Us</h2>
      <p><strong>Business:</strong> Shlok Enterprise</p>
      <p><strong>Mobile:</strong> <a href="tel:+919026542364">9026542364</a></p>
      <p>We look forward to hearing from you.</p>
      <a class="button" href="https://wa.me/919026542364" target="_blank" rel="noopener noreferrer">
        Chat on WhatsApp
      </a>
    </section>
  </main>

  <footer>
    <p>&copy; 2026 Shlok Enterprise. All Rights Reserved.</p>
  </footer>

  <a class="whatsapp" href="https://wa.me/919026542364" target="_blank" rel="noopener noreferrer" aria-label="Chat with Shlok Enterprise on WhatsApp">
    WhatsApp
  </a>
</body>
</html>'''


@app.route("/")
def home():
    return render_template_string(PAGE)


if __name__ == "__main__":
    # Run locally at http://127.0.0.1:5000
    app.run(host="127.0.0.1", port=5000, debug=True)
