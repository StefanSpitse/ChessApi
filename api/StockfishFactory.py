from stockfish import Stockfish


class StockfishFactory:
    def __init__(self, path, elo, depth, visualize):
        self.path = path  # Path to stockfish
        self.elo = elo  # At what elo rating the stockfish is playing (how strong he is)
        self.depth = depth  # How many steps is stockfish thinking ahead (the higher the number the more cpu intesive
        self.visualize = visualize  # If the user wants a visualized board on request
        self.stockfish = Stockfish(path=self.path)  # Stockfish engine

    def GatherMoves(self, rep: int = 1):
        parse = []
        for i in range(rep):
            parse.append({i: self.GetBestMove(), "evaluation": self.stockfish.get_evaluation()})

        return parse

    def GetBestMove(self):
        best = self.stockfish.get_best_move()
        self.stockfish.make_moves_from_current_position([best])
        return self.stockfish.get_top_moves(1)[0]
