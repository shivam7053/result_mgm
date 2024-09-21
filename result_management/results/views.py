from django.shortcuts import render
from .models import StudentResult

def student_results(request):
    results = StudentResult.objects.all()

    # Apply filters based on GET parameters
    college = request.GET.get('college')
    stream = request.GET.get('stream')
    batch = request.GET.get('batch')
    semester = request.GET.get('semester')

    if college:
        results = results.filter(college=college)
    if stream:
        results = results.filter(stream=stream)
    if batch:
        results = results.filter(batch=batch)
    if semester:
        results = results.filter(semester=semester)

    # Group results by university_roll_no to calculate CGPA
    student_data = {}
    for result in results:
        if result.university_roll_no not in student_data:
            student_data[result.university_roll_no] = {
                'name': result.student_name,
                'college': result.college,
                'stream': result.stream,
                'batch': result.batch,
                'semesters': []
            }
        student_data[result.university_roll_no]['semesters'].append({
            'semester': result.semester,
            'cgpa': result.cgpa,
        })

    return render(request, 'results/student_results.html', {'student_data': student_data})
