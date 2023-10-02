from Travelagent import TravelAgent

class main:
    travel_agent = TravelAgent('Go Jayan')
    trip_info1 = travel_agent.set_trip_one_city_one_way('DAC','PRA','24/08/23')
    
    # print('aircraft details =>', trip_info1.aircraft)
    # print('price =>', trip_info1.price)

    trip_cities = ['DUB', 'LHR', 'SYD', 'JFK']
    trip_info2 = travel_agent.set_trip_multi_city_flexible_route(trip_cities,'24/08/23')
    for trip in trip_info2[0]:
        print(trip)
    print("minimum price = ", trip_info2[1])
    
if __name__ == 'main':
    main()