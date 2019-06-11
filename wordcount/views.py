from django.shortcuts import render

# Create your views here. #home은 home.html을 말하는것
def home(request):
    return render(request, 'home.html')
def count(request):
    full_text = request.GET['fulltext']
    word_list = full_text.split() #문자열을 분리한 후, 리스트로 저장하는 함수
    
    word_dictionary = {} #빈 딕셔너리 생성


    for word in word_list:
        if word in word_dictionary:
            word_dictionary[word] += 1 #단어가 존재한다면 카운트
        else :
            word_dictionary[word] = 1 #처음 나오는 단어이면 key와 value 등록

    return render(request, 'count.html', {'fulltext': full_text, 'total': len(word_list), 'dictionary': word_dictionary.items() })