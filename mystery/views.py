from django.shortcuts import render, redirect
from datetime import datetime
from django.http import JsonResponse
from . import keys

def landing_page(request):
    return render(request, 'mystery/landing.html')

def puzzle_level_1(request):
    if request.method == 'POST':
        answer = request.POST.get('answer', '').lower().strip()
        if answer == keys.LEVEL_1_KEY:  # Answer to the first puzzle
            return JsonResponse({'success': True})
        return JsonResponse({'success': False})
    return render(request, 'mystery/puzzle1.html')

def puzzle_level_2(request):
    if request.method == 'POST':
        answer = request.POST.get('answer', '').lower().strip()
        if answer == keys.LEVEL_2_KEY:  # Answer to the second puzzle
            return JsonResponse({'success': True})
        return JsonResponse({'success': False})
    return render(request, 'mystery/puzzle2.html')

def puzzle_level_3(request):
    if request.method == 'POST':
        answer = request.POST.get('answer', '').lower().strip()
        if answer == keys.LEVEL_3_KEY:  # Answer to the third puzzle
            return JsonResponse({'success': True})
        return JsonResponse({'success': False})
    return render(request, 'mystery/puzzle3.html')

def reveal_page(request):
    current_date = datetime.now()
    target_date = datetime(*keys.TARGET_DATE)
    can_reveal = current_date >= target_date
    return render(request, 'mystery/reveal.html', {'can_reveal': can_reveal})
