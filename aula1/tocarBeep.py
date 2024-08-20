from app import sound as som
import runloop as Lego  
async def main():
    await som.beep(400,1000,100)
Lego.run(main())