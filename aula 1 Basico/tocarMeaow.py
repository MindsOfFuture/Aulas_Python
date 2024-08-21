from app import sound as som
import runloop as Lego  
async def main():
    await som.play("Cat Meow 1")
Lego.run(main())