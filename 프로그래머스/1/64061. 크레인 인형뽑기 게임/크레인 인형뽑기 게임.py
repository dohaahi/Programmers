def solution(board, moves):
    answer = 0
    basket = []

    for n in moves:
        for i in range(len(board)):
            doll = board[i][n - 1]

            if doll != 0:
                board[i][n - 1] = 0

                # 바구니에 인형이 없는 경우
                if len(basket) == 0:
                    basket.append(doll)
                    break

                # 뽑은 인형이 바구니에 있는 인형과 다른 경우
                elif basket[-1] != doll:
                    basket.append(doll)
                    break

                # 뽑은 인형이 바구니에 있는 인형과 같은 경우
                # 바구니에 있는 인형 터짐 + answer 증가
                elif basket[-1] == doll:
                    basket.pop()
                    answer += 2
                    break
                    
    return answer