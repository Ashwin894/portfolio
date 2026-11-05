from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse


# Create your views here.
class About(View):
    def get(self,request):
        data={
            "ID":10,
            "Full Name":"Ashwin Thomas",
            "Professional Title":"Python developer",
            "Bio":"Open to work",
            "DOB":"2002-08-19",
            "Email":"ashwinthomas72@gmail.com",
            "Contact Number":7356442764,
            "Location":"Kochi",
            "Github_URL":"https://github.com/AswinAnil1110",
            "Linkedin_URL":"https://linkedin.com/AswinAnil1110"
        }
        return JsonResponse(data)
class Education(View):
    def get(self,request):
        data={
            "ID":1,
            "Institution":"MGAJ",
            "Degree/Course":"BCA",
            "University":"MGU",
            "Location":"Kochi",
            "Start_year":2023,
            "End_year":2026,
            "Grade_or_CGPA":5.8,
            "Description":"Tough subject"
        }
        return JsonResponse(data)
class ProjectView(View):
    def get(self,request):
        data=[
            {
                "ID":1,
                "Title":"Firstaid",
                "Short_description":"First_Aid_description",
                "Technologies_used":["Python","Django","Google GenAI SDK"],
                "Live_url":"https://first_aid.example.com",
                "Github_URL":"https://github.com/yourusername/firstaid",
                "Image_URL":"htpps://api.yourdomain.com/media/projects/first_aid",
                "Featured":True
            },
            {
               "ID":2,
                "Title":"Foodbox",
                "Short_description":"Foodbox_description",
                "Technologies_used":["Python","Django","Google GenAI SDK"],
                "Live_url":"https://foodbox.example.com",
                "Github_URL":"https://github.com/yourusername/foodbox",
                "Image_URL":"https://api.yourdomain.com/media/projects/foodbox",
                "Featured":True
            },
            {
                "ID":3,
                "Title":"Moviepox",
                "Short_description":"Movie_description",
                "Technologies_used":["Python","Django","Google GenAI SDK"],
                "Live_url":"https://moviepox.example.com",
                "Github_URL":"https://github.com/yourusername/moviepox",
                "Image_URL":"https://api.yourdomain.com/media/projects/moviepox",
                "Featured":True
            }
        ]
        return JsonResponse(data,safe=False)
class SkillsView(View):
    def get(self,request):
        data=[
            {
                "ID":1,
                "Skill_Name":"Python",
                "Category":"Python programmer",
                "Proficiency":"Advanced",
                "Years_of_experience":4
            },
            {
               "ID":2,
                "Skill_Name":"Django",
                "Category":"Backend",
                "Proficiency":"Beginer",
                "Years_of_experience":1 
            },
            {
                "ID":3,
                "Skill_Name":"React",
                "Category":"Frontend",
                "Proficiency":"Advanced",
                "Years_of_experience":5
            }
        ]
        return JsonResponse(data,safe=False)
class ExperienceView(View):
    def get(self,request):
        data=[
            {
                "ID":10,
                "Job_title":"Software developer",
                "Company_Name":"Infosys",
                "Location":"Kakkanad",
                "Employment_type":"Remote",
                "Start_date":"2024-08-11",
                "End_date":"2026-05-23",
                "Currently_working":"No",
                "Description":"Looking for job."
            },
            {
                "ID":20,
                "Job_title":"Python developer",
                "Company_Name":"Wipro",
                "Location":"Kochi",
                "Employment_type":"on Office",
                "Start_date":"2020-07-11",
                "End_date":"2023-05-23",
                "Currently_working":"Yes",
                "Description":"Currently working python developer on Amazon"
            },
            {
                "ID":30,
                "Job_title":"Devops engineer",
                "Company_Name":"Google",
                "Location":"USA",
                "Employment_type":"Remote",
                "Start_date":"2026-08-08",
                "End_date":"Working",
                "Currently_working":"Yes",
                "Description":"Working Employee"
            }
        ]
        return JsonResponse(data,safe=False)
class CertificateView(View):
    def get(self,request):
        data=[
            {
                "ID":1,
                "Certification_Name":"Python",
                "Issuing_Organization":"Luminar",
                "Issued_date":"2027-01-02",
            },
            {
               "ID":10,
                "Certification_Name":"Data analyst",
                "Issuing_Organization":"Luminar",
                "Issued_date":"2027-01-02",
            }
        ]
        return JsonResponse(data,safe=False)
class ServicesView(View):
    def get(self,request):
        data=[
            {
                "ID":12,
                "Service_Name":"Digital marketing",
                "Description":"Managing social media platforms",
                "Technologies_used":"AI"
            },
            {
                "ID":4,
                "Service_Name":"Python developer",
                "Description":"Creating web applications using python",
                "Technologies_used":["Python","AI","HTML"]
            }
        ]
        return JsonResponse(data,safe=False)