## 34_workshop (19.04.25)

### 아래의 두 코드에 적절한 데코레이터를 작성하여 허용되지 않은 HTTP Method의 경우 405 Method Not Allowed 상태코드를 반환하도록 하시오.

```python
def create(request):
    if request.method == 'POST':
        board_form = BoardForm(request.POST)
        if board_form.is_valid():
            board - board_form.save()
            return redirect(board)
	else:
        board_form = BoardForm()
        context = {
            'board_form':borad_form
        }
	return render(request, 'boards/form.html', context)


def delete(request, board_pk):
    if request.method == 'POST':
        board = get_object_or_404(Board, pk=board_pk)
        board.delete()
        return redirect('boards:index')
```