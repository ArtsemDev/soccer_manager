from datetime import date

from sqlalchemy import or_

from model import City, Team, Position, Footballer


print(Footballer.join(City, City.pk.__eq__(1)))
# # Team(name='КотикиНаркотики').save()
# Position(name='полурыба полухуй').save()
# Footballer(full_name='Ебанько', date_of_birth=date(year=1999, month=2, day=1), team_id=1, city_id=1, position_id=1).save()
# with session() as session:
#     city = City(name='Moscow')
#     session.add(city)
#     session.commit()
#     session.refresh(city)
# print(city.pk)
# print(city.name)

# with session() as session:
#     session.scalars(
#         select(City)
#         .filter(City.pk.__gt__())
#     )
    # city = session.get(City, 1)
    # city.name = 'Минск'
    # session.add(city)
    # session.commit()
    # session.delete(city)
    # session.commit()
    # print(city.name)
    # response = session.scalars(
    #     select(City)
    #     .filter(City.pk >= 1)
    #     .order_by(City.name.asc())
    # )
    # print(response.all())

    # cities = [City(name='Gomel'), City(name='Mogilev')]
    # session.add_all(cities)
    # session.commit()