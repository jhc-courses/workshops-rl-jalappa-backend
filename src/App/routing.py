from flask_cors import CORS
from flask import Flask, jsonify, request

app = Flask(__name__)
CORS(app)

# Initial course data
courses = [
    {
        "course_id": 1,
        "title": "AWS Solutions Architect Associate",
        "description": "Gain practical hands-on experience and leverage architectural best practices to design and deploy scalable systems on AWS.",
        "photo": "https://adminappapis-publicdatabucket3968349e-bea8cnueqwrl.s3.ap-south-1.amazonaws.com/courses/aws-solutions-architect-associate/Aws-Solutions-Architect-Associate.jpg",
        "tamps_up": 0,
        "tamps_down": 0
    },
    {
        "course_id": 2,
        "title": "Azure Administration",
        "description": "The Microsoft Azure training is in-depth training for the Azure Administrator certification that will help you master cloud architecture, components, Resource Manager, Virtual Network connectivity, deploying the cloud infrastructure, and security.",
        "photo": "https://adminappapis-publicdatabucket3968349e-bea8cnueqwrl.s3.ap-south-1.amazonaws.com/courses/azure-administration/Azure-Administration.jpg",
        "tamps_up": 0,
        "tamps_down": 0
    },
    {
        "course_id": 3,
        "title": "Azure Devops",
        "description": "Our Azure DevOps course is designed to equip you with the skills and knowledge needed to effectively utilize Azure DevOps for continuous integration, delivery, and deployment. Through hands-on exercises and real-world scenarios, you'll learn to automate the build and release pipelines, manage source control, and implement agile methodologies. By the end of the course, you'll have a deep understanding of Azure DevOps and the ability to apply it to streamline software delivery processes.",
        "photo": "https://adminappapis-publicdatabucket3968349e-bea8cnueqwrl.s3.ap-south-1.amazonaws.com/courses/azure-devops/Azure-Devops.jpg",
        "tamps_up": 0,
        "tamps_down": 0
    },
    {
        "course_id": 4,
        "title": "Java/J2EE",
        "description": "Become proficient in Java programming, enabling you to write efficient, maintainable code for diverse applications by the course's end.",
        "photo": "https://adminappapis-publicdatabucket3968349e-bea8cnueqwrl.s3.ap-south-1.amazonaws.com/courses/core-java/Core-Java.jpg",
        "tamps_up": 0,
        "tamps_down": 0
    },
    {
        "course_id": 5,
        "title": "DevOps Master Course",
        "description": "Comprehensive training covering the principles, practices, and tools used in DevOps to enable efficient software development, delivery, and operations in organizations.",
        "photo": "https://adminappapis-publicdatabucket3968349e-bea8cnueqwrl.s3.ap-south-1.amazonaws.com/courses/devops-master-course/Devops-Master-Course.jpg",
        "tamps_up": 0,
        "tamps_down": 0
    },
    {
        "course_id": 6,
        "title": "Kubernetes Master Course",
        "description": "Comprehensive Kubernetes course covering architecture, deployment, security, and more. Gain hands-on experience managing containerized applications.",
        "photo": "https://adminappapis-publicdatabucket3968349e-bea8cnueqwrl.s3.ap-south-1.amazonaws.com/courses/kubernetes/Kubernetes.jpg",
        "tamps_up": 0,
        "tamps_down": 0
    },
    {
        "course_id": 7,
        "title": "Python Scripting",
        "description": "Become proficient in Python scripting, enabling you to write efficient, maintainable code for diverse applications by the course's end.",
        "photo": "https://adminappapis-publicdatabucket3968349e-bea8cnueqwrl.s3.ap-south-1.amazonaws.com/courses/python-scripting/Python-Scripting.jpg",
        "tamps_up": 0,
        "tamps_down": 0
    },
    {
        "course_id": 8,
        "title": "React JS",
        "description": "The ReactJS Course trains learners to build dynamic web apps using React, a popular and efficient JavaScript library known for its component-based architecture.",
        "photo": "https://adminappapis-publicdatabucket3968349e-bea8cnueqwrl.s3.ap-south-1.amazonaws.com/courses/react-js/React-Js.jpg",
        "tamps_up": 0,
        "tamps_down": 0
    },
    {
        "course_id": 9,
        "title": "Terraform Certification",
        "description": "Terraform Certification Course: In-depth training on Terraform for infrastructure provisioning, management, and automation in the cloud.",
        "photo": "https://adminappapis-publicdatabucket3968349e-bea8cnueqwrl.s3.ap-south-1.amazonaws.com/courses/terraform-certification/Terraform-Certification.jpg",
        "tamps_up": 0,
        "tamps_down": 0
    }
]

# API endpoint for updating tamps up and tamps down for a course
@app.route('/update_tamps/<int:course_id>', methods=['PUT'])
@cross_origin()
def update_tamps(course_id):
    global courses

    data = request.json

    for course in courses:
        if course['course_id'] == course_id:
            if 'action' in data and 'count' in data:
                action = data['action']

                if action == 'up':
                    course['tamps_up'] += data['count']
                elif action == 'down':
                    course['tamps_down'] += data['count']
                else:
                    return jsonify({"error": "Invalid action. Use 'up' or 'down'."}), 400

                return jsonify({"tamps_up": course['tamps_up'], "tamps_down": course['tamps_down']})
            else:
                return jsonify({"error": "Missing required fields 'action' and 'count'."}), 400

    return jsonify({"error": "Course not found."}), 404

# API endpoint for retrieving information about all courses
@app.route('/all_courses', methods=['GET'])
@cross_origin()
def all_courses():
    result = []
    for course in courses:
        total_votes = course["tamps_up"] + course["tamps_down"]
        rating = 0 if total_votes == 0 else course["tamps_up"] / total_votes * 100
        result.append({
            "course_id": course["course_id"],
            "title": course["title"],
            "tamps_up": course["tamps_up"],
            "tamps_down": course["tamps_down"],
            "total_votes": total_votes,
            "rating": rating,
            "description": course["description"],
            "photo": course["photo"]
        })
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5002)
