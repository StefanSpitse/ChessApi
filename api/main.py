from fastapi import FastAPI, Path, Query
from StockfishFactory import StockfishFactory
import pandas as pd

app = FastAPI()


@app.get("/stockfish")
async def Request(position: str, repeated: int = 1, amount: int = Query(1, le=5, gt=1)):
    if position == "":
        return {"big test"}

    else:

        bestmove = StockfishFactory(
            "C:\\Users\\Stefa\\OneDrive\\School\\Semester "
            "2\\Python\\StockfishAPI\\stockfish\\stockfish-windows-x86-64-modern.exe",
            1500, 10, amount)
        return bestmove.GatherMoves(repeated)
