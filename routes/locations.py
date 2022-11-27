from fastapi import APIRouter
location = APIRouter()
from sqlalchemy import func, insert, select, update,delete, and_, or_
from schemas.locations import Location
from config.db import get_db
from models.locations import Location as location_model
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

def getlocation(db: Session, location_id: int ):
    select_statement = select(location_model).where(location_model.id == location_id)
    result = Location.from_orm(db.execute(select_statement).unique().scalar())
    return result


@location.get("/")   
async def heath_check():
    
    return {"health": True}


#get location
@location.get("/location/{id}")
async def read_data_id(id: int, db: Session = Depends(get_db)):
        select_statement = select(location_model)
        result = db.execute(select_statement).unique(id).scalar()
        return result

@location.get("/location")
async def read_data_distance(latitude: float, longitude: float, distance_in_km: float, db: Session = Depends(get_db)):
    

    select_statement = select(location_model).where(func.acos(func.sin(func.radians(latitude)) *
         func.sin(func.radians(location_model.latitude)) + func.cos(func.radians(latitude)) *
          func.cos(func.radians(location_model.latitude)) * func.cos(func.radians(location_model.longitude) -
         (func.radians(longitude)))) * 6371 <= distance_in_km)
    result = db.execute(select_statement).scalars().unique().all()
    result = [Location.from_orm(item) for item in result]

    return result


@location.post("/location")
async def write_data(location : Location,  db: Session = Depends(get_db)):
    create_stmt = insert(location_model).values(**location.dict())

    try:
        db.execute(create_stmt)
        db.commit()
    except Exception as exe:
        raise exe
   # return db.execute(location_model.select()).fetchall()
    return getlocation(db,location.id)


@location.put("/location/{locat_id}")
async def update_data(locat_id:int,location: Location, db: Session = Depends(get_db)):

  update_stat = update(location_model).where(location_model.id == location.id).values(**location.dict())

  try:
        db.execute(update_stat)
        db.commit()
  except Exception as exe:
        raise exe
   # return db.execute(location_model.select()).fetchall()
  return getlocation(db,locat_id)
  



@location.delete("/location/{locat_id}")
async def delete_data(locat_id:int, db: Session = Depends(get_db)):
    delete_stat = delete(location_model).where(location_model.id == locat_id)

    try:
        db.execute(delete_stat)
        db.commit()
    except Exception as exe:
        raise exe
   # return db.execute(location_model.select()).fetchall()
    return {"msg":"deleted"}

