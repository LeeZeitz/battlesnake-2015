curl -X POST -H "Content-Type: application/json" -d '{"game_id": "hairy-cheese", "width": 10, "height": 10 }' http://localhost:8080/start
printf "\n"
curl -X POST -H "Content-Type: application/json" -d '{"game_id": "hairy-cheese", "turn": 4, "snakes": [ { "name": "crazySnake", "state": "alive", "taunt": "", "age": 56, "score": 8, "coords": [ [1, 0], [0, 0], [0, 1], [0, 2] ]}, {  "name": "dummysnake", "state": "alive", "taunt": "", "score": 8, "coords": [ [2, 2], [2, 1], [3, 1], [3, 0] ] }], "food": [ [2, 0] ] }' http://localhost:8080/move
printf "\n"
