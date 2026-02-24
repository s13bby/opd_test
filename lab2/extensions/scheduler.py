from apscheduler.schedulers.asyncio import AsyncIOScheduler
from extensions import db
import main
#---------------------------------------------------------------------------------------
tasker = AsyncIOScheduler()
#---------------------------------------------------------------------------------------
async def reward_job():
    users = db.get_all_users()
    for user_id in users:
        balance = db.get(user_id, "balance")
        db.set_(user_id, balance + main.HOW_MUCH_ADDED_COINS, "balance")
#---------------------------------------------------------------------------------------
async def decreese():
    users = db.get_all_users()
    for user_id in users:
        comfort = db.get(user_id, "comfort")
        comfort = db.get(user_id, "food")
        comfort = db.get(user_id, "water")

        if (comfort - main.HOW_MUCH_REMOVE_COMFORT) < 0:
            db.set_(user_id,comfort - main.HOW_MUCH_REMOVE_COMFORT, "comfort")
        else:
            db.set_(user_id,0,"comfort")
        
        if (comfort - main.HOW_MUCH_REMOVE_FOOD) < 0:
            db.set_(user_id,comfort - main.HOW_MUCH_REMOVE_COMFORT, "food")
        else:
            db.set_(user_id,0,"food")

        if (comfort - main.HOW_MUCH_REMOVE_WATER) < 0:
            db.set_(user_id,comfort - main.HOW_MUCH_REMOVE_COMFORT, "water")
        else:
            db.set_(user_id,0,"water")
        