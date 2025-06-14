from weasyprint import HTML, CSS
import os

def generate_resume_pdf():
    # Ensure the static directory exists
    os.makedirs('static', exist_ok=True)
    
    # Read the HTML file
    with open('templates/resume.html', 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # Create PDF
    HTML(string=html_content).write_pdf(
        'static/resume.pdf',
        stylesheets=[],
        presentational_hints=True
    )
    
    print("Resume PDF generated successfully!")

if __name__ == '__main__':
    generate_resume_pdf() 