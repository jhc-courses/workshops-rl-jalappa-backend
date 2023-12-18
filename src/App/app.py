from flask import Flask, render_template ,request

app = Flask(__name__)

# Sample data for different courses
courses = [
    {
        'title': 'AWS Solutions Architect Associate',
        'description': 'Gain practical hands-on experience and leverage architectural best practices to design and deploy scalable systems on AWS.',
        'photo': 'https://adminappapis-publicdatabucket3968349e-bea8cnueqwrl.s3.ap-south-1.amazonaws.com/courses/aws-solutions-architect-associate/Aws-Solutions-Architect-Associate.jpg'
    },
    {
        'title': 'Azure Administration',
        'description': 'The Microsoft Azure training is in-depth training for the Azure Administrator certification that will help you master cloud architecture, components, Resource Manager, Virtual Network connectivity, deploying the cloud infrastructure, and security.',
        'photo': 'https://adminappapis-publicdatabucket3968349e-bea8cnueqwrl.s3.ap-south-1.amazonaws.com/courses/azure-administration/Azure-Administration.jpg'
    },
    {
        'title': 'Azure Devops',
        'description': 'Our Azure DevOps course is designed to equip you with the skills and knowledge needed to effectively utilize Azure DevOps for continuous integration, delivery, and deployment. Through hands-on exercises and real-world scenarios, you\'ll learn to automate the build and release pipelines, manage source control, and implement agile methodologies. By the end of the course, you\'ll have a deep understanding of Azure DevOps and the ability to apply it to streamline software delivery processes.',
        'photo': 'https://adminappapis-publicdatabucket3968349e-bea8cnueqwrl.s3.ap-south-1.amazonaws.com/courses/azure-devops/Azure-Devops.jpg'
    },
    {
        'title': 'Java/J2EE',
        'description': 'Become proficient in Java programming, enabling you to write efficient, maintainable code for diverse applications by the course\'s end.',
        'photo': 'https://adminappapis-publicdatabucket3968349e-bea8cnueqwrl.s3.ap-south-1.amazonaws.com/courses/core-java/Core-Java.jpg'
    },
    {
        'title': 'DevOps Master Course',
        'description': 'Comprehensive training covering the principles, practices, and tools used in DevOps to enable efficient software development, delivery, and operations in organizations.',
        'photo': 'https://adminappapis-publicdatabucket3968349e-bea8cnueqwrl.s3.ap-south-1.amazonaws.com/courses/devops-master-course/Devops-Master-Course.jpg'
    },
    {
        'title': 'Kubernetes Master Course',
        'description': 'Comprehensive Kubernetes course covering architecture, deployment, security, and more. Gain hands-on experience managing containerized applications.',
        'photo': 'https://adminappapis-publicdatabucket3968349e-bea8cnueqwrl.s3.ap-south-1.amazonaws.com/courses/kubernetes/Kubernetes.jpg'
    },
    {
        'title': 'Python Scripting',
        'description': 'Become proficient in Python scripting, enabling you to write efficient, maintainable code for diverse applications by the course\'s end.',
        'photo': 'https://adminappapis-publicdatabucket3968349e-bea8cnueqwrl.s3.ap-south-1.amazonaws.com/courses/python-scripting/Python-Scripting.jpg'
    },
    {
        'title': 'React JS',
        'description': 'The ReactJS Course trains learners to build dynamic web apps using React, a popular and efficient JavaScript library known for its component-based architecture.',
        'photo': 'https://adminappapis-publicdatabucket3968349e-bea8cnueqwrl.s3.ap-south-1.amazonaws.com/courses/react-js/React-Js.jpg'
    },
    {
        'title': 'Terraform Certification',
        'description': 'Terraform Certification Course: In-depth training on Terraform for infrastructure provisioning, management, and automation in the cloud.',
        'photo': 'https://adminappapis-publicdatabucket3968349e-bea8cnueqwrl.s3.ap-south-1.amazonaws.com/courses/terraform-certification/Terraform-Certification.jpg'
    }
]

# Route for handling only GET requests and displaying all courses
@app.route('/all_course', methods=['GET'])
def all_courses():
    return courses

if __name__ == '__main__':
    app.run(debug=True)
    app.run(debug=True, host="0.0.0.0", port=5001)


