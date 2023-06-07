import chess
import dates

dates.date_validator_cmd()

coords = [(1,2),(2,4),(3,6),(4,8),(5,3),(6,1),(7,7),(8,5)]
print(chess.check_8_queens(coords))


coords = chess.generate_8_queens()
print(coords)

res = chess.check_8_queens(coords)
print('Эти координаты являются регением' if res else 'Эти координаты не являются решением')