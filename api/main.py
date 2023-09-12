from fastapi import FastAPI
from StockfishFactory import StockfishFactory
import pandas as pd

app = FastAPI()


@app.get("/stockfish")
async def Request(position: str, repeated: int = 1, visualize: bool = False):
    if position == "":
        return {"big test"}

    else:

        bestmove = StockfishFactory(
            "C:\\Users\\Stefa\\OneDrive\\School\\Semester "
            "2\\Python\\StockfishAPI\\stockfish\\stockfish-windows-x86-64-modern.exe",
            1500, 10)
        return bestmove.GatherMoves(repeated)
