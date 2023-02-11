from django.shortcuts import render


def board(request):
    '''
        placeholder function to render the board tenplate
    '''
    return render(request, "chess/board.html")