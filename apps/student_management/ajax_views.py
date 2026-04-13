from .models import Student
import json
import os
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import base64
from django.core.files.base import ContentFile
from django.urls import reverse

@csrf_exempt
def update_student_profile_picture(request):
    try: 
        # parse the JSON body
        data = json.loads(request.body)

        student_id = data.get("student_id")
        image_data = data.get("image_data")

        if not student_id or not image_data:
            return JsonResponse(
                {"success": False, "message": "invalid data."},
                status=400
            )
        
        # Find the student by ID (UUID)
        try:
            student = Student.objects.get(id=student_id)
        except Student.DoesNotExist:
            return JsonResponse(
                {"success": False, "message": "student not found."},
                status=404
           )
    
        extension = None

        # Handle base64 prefix and determine extension
        if image_data.startswith("data:image/jpeg;base64,"):
            image_data = image_data[len("data:image/jpeg;base64,"):]
            extension = ".jpg"
        elif image_data.startswith("data:image/png;base64,"):
            image_data = image_data[len("data:image/png;base64,"):]
            extension = ".png"
        else: 
            return JsonResponse(
            {"success": False, "message": "Unsupported image format. Only JPG and PNG are allowed"},
            status=400
        )   

        # decode base64 string
        try:
            image_data_decoded = base64.b64decode(image_data)
        except Exception:
            return JsonResponse(
                {"success": False, "message": "Invalid image data."},
                status=404
           )
        
        # generate the file name
        file_name = f"{student.id}{extension}"

        #delete old photo files if exists
        if student.photo:
            old_file_path = student.photo.path
            if os.path.exists(old_file_path):
                try:
                    os.remove(old_file_path)
                except Exception as e:
                    # log the error but continue
                    print(f"Could not delete old file: {e}")    

        #wrap decoded bytes in ContentFiles and save to the imagefield
        profile_picture = ContentFile(image_data_decoded) 
        student.photo.save(file_name, profile_picture, save=True) 

        # Redirect back to the student profile
        redirect_url = reverse("students:student_profile", args=[student.id])  

        return JsonResponse(
        {"success": True, "message": "Profile picture updated successfully", "redirect_url": redirect_url}
        )         
    except json.JSONDecodeError:
        return JsonResponse(
        {"success": False, "message": "Invalid JSON data"},
        status=400
        )

    except Exception as e:
        return JsonResponse(
        {"success": False, "message": f"Server error: {str(e)}"},
        status=500
        )