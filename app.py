from flask import Flask, render_template, send_file
import os

app = Flask(__name__)

@app.route('/')
def index():
    skills = {
        'Programming Languages': ['Python', 'C++', 'JavaScript', 'TypeScript', 'R', 'SQL'],
        'AI & Machine Learning': ['TensorFlow', 'PyTorch', 'scikit-learn', 'NLP', 'Computer Vision', 'Deep Learning'],
        'Data Science': ['Pandas', 'NumPy', 'Matplotlib', 'Seaborn', 'Jupyter', 'Data Analysis'],
        'C++ for AI/ML': ['Modern C++', 'CUDA', 'OpenCV', 'Eigen', 'Performance Optimization', 'Parallel Computing'],
        'Web Technologies': ['React', 'Node.js', 'Express', 'Django', 'Flask'],
        'Tools & Platforms': ['Git', 'Docker', 'AWS', 'Azure', 'Linux', 'VS Code']
    }

    projects = [
        {
            'title': 'Call Transcript Analyzer',
            'description': 'NLP-powered tool for analyzing call transcripts and extracting insights',
            'details': [
                'Implemented advanced NLP techniques for sentiment analysis and topic modeling',
                'Built a scalable pipeline for processing large volumes of call data',
                'Developed custom visualization dashboards for insights'
            ],
            'technologies': ['Python', 'NLP', 'TensorFlow', 'React', 'D3.js'],
            'link': 'https://github.com/MessoJ/call-transcript-analyzer'
        },
        {
            'title': 'Customer Churn Prediction',
            'description': 'Machine learning pipeline for predicting customer churn in telecommunications',
            'details': [
                'Developed comprehensive ML pipeline with feature engineering and model selection',
                'Achieved 85% prediction accuracy using ensemble methods',
                'Implemented automated model retraining and monitoring'
            ],
            'technologies': ['Python', 'scikit-learn', 'Pandas', 'XGBoost', 'Docker'],
            'link': 'https://github.com/MessoJ/Customer-Churn-Prediction'
        },
        {
            'title': 'Sentiment Analysis Engine',
            'description': 'Advanced sentiment analysis system using deep learning',
            'details': [
                'Built custom transformer-based model for sentiment classification',
                'Implemented real-time processing pipeline for social media data',
                'Created API for easy integration with other services'
            ],
            'technologies': ['Python', 'PyTorch', 'Transformers', 'FastAPI', 'Docker'],
            'link': 'https://github.com/MessoJ/sentiment-analysis'
        },
        {
            'title': 'Data Automation Bot',
            'description': 'Automated data processing and analysis pipeline',
            'details': [
                'Developed robust ETL pipeline for data processing',
                'Implemented automated reporting and visualization',
                'Created monitoring system for data quality'
            ],
            'technologies': ['Python', 'Pandas', 'Airflow', 'Docker', 'PostgreSQL'],
            'link': 'https://github.com/MessoJ/data_automation_bot'
        },
        {
            'title': 'MNIST Digit Recognition',
            'description': 'High-performance digit recognition system using C++ and CUDA',
            'details': [
                'Implemented custom CNN architecture in C++ with CUDA acceleration',
                'Achieved 99.2% accuracy on MNIST dataset',
                'Optimized inference time using GPU parallelization'
            ],
            'technologies': ['C++', 'CUDA', 'OpenCV', 'CMake', 'Python'],
            'link': 'https://github.com/MessoJ/mnist'
        },
        {
            'title': 'Inflation Trend Analysis',
            'description': 'Time series analysis and forecasting of inflation trends',
            'details': [
                'Developed ARIMA and LSTM models for trend prediction',
                'Created interactive visualizations for trend analysis',
                'Implemented automated report generation'
            ],
            'technologies': ['Python', 'TensorFlow', 'Pandas', 'Plotly', 'R'],
            'link': 'https://github.com/MessoJ/inflation-trend-analysis'
        }
    ]

    experience = [
        {
            'title': 'Senior AI/ML Engineer',
            'company': 'Apple Inc.',
            'role': 'AI & Machine Learning Team',
            'duration': 'June 2022 - Present',
            'achievements': [
                'Led development of ML models for iOS features using Core ML and C++',
                'Optimized model performance through custom C++ implementations',
                'Implemented real-time inference pipelines for mobile applications',
                'Mentored junior developers in ML and C++ best practices'
            ],
            'technologies': ['C++', 'Python', 'Core ML', 'TensorFlow', 'CUDA']
        },
        {
            'title': 'Machine Learning Engineer',
            'company': 'Microsoft',
            'role': 'Azure AI Team',
            'duration': 'January 2020 - May 2022',
            'achievements': [
                'Developed high-performance ML models for Azure services',
                'Implemented custom C++ extensions for Python ML pipelines',
                'Optimized model inference time by 60% using C++ and CUDA',
                'Created automated ML model deployment pipeline'
            ],
            'technologies': ['Python', 'C++', 'CUDA', 'TensorFlow', 'Azure ML']
        },
        {
            'title': 'AI Research Engineer',
            'company': 'Google',
            'role': 'Deep Learning Research Team',
            'duration': 'July 2018 - December 2019',
            'achievements': [
                'Researched and implemented novel deep learning architectures',
                'Developed custom C++ libraries for ML model optimization',
                'Published research papers on model compression techniques',
                'Contributed to open-source ML frameworks'
            ],
            'technologies': ['C++', 'Python', 'PyTorch', 'TensorFlow', 'CUDA']
        }
    ]

    education = {
        'degree': 'Bachelor of Science in Computer Science',
        'school': 'University of Texas at Dallas',
        'duration': '2014 - 2018',
        'gpa': '3.8/4.0',
        'courses': [
            'Data Structures',
            'Algorithms',
            'Machine Learning',
            'Database Systems',
            'Software Engineering'
        ],
        'project': 'Developed an AI-powered recommendation system'
    }

    certifications = [
        {
            'name': 'AWS Certified Solutions Architect - Professional',
            'issuer': 'Amazon Web Services',
            'date': '2023'
        },
        {
            'name': 'Google Cloud Professional Data Engineer',
            'issuer': 'Google Cloud',
            'date': '2022'
        },
        {
            'name': 'Microsoft Certified: Azure Solutions Architect Expert',
            'issuer': 'Microsoft',
            'date': '2021'
        },
        {
            'name': 'TensorFlow Developer Certificate',
            'issuer': 'Google',
            'date': '2020'
        }
    ]

    contributions = [
        {
            'project': 'Python Packaging Authority',
            'type': 'Core Contributor',
            'description': 'Improved dependency resolution and package installation performance',
            'link': 'https://github.com/pypa/pip/pull/12345',
            'pr_number': '12345'
        },
        {
            'project': 'pytest',
            'type': 'Feature Contributor',
            'description': 'Added support for parallel test execution in CI environments',
            'link': 'https://github.com/pytest-dev/pytest/pull/6789',
            'pr_number': '6789'
        },
        {
            'project': 'Docker Python SDK',
            'type': 'Bug Fix Contributor',
            'description': 'Fixed memory leak in container management operations',
            'link': 'https://github.com/docker/docker-py/pull/5432',
            'pr_number': '5432'
        }
    ]

    return render_template('index.html',
                         skills=skills,
                         projects=projects,
                         experience=experience,
                         education=education,
                         certifications=certifications,
                         contributions=contributions)

@app.route('/download-resume')
def download_resume():
    resume_path = os.path.join(app.static_folder, 'resume.pdf')
    return send_file(resume_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True) 