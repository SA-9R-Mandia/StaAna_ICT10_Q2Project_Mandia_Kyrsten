from pyscript import display, document

club_info = {
            "math": {
                "name": "Math Club",
                "description": "A club for people who really like math :)",
                "meeting_time": "Every Wednesday 1:30-5:00 PM",
                "location": "Room 222",
                "advisor": "Mr. Pythagoras",
                "members": 30,
                "category": "Academic"
            },
            "drama": {
                "name": "Drama Club",
                "description": "For people who really like theatre arts :)",
                "meeting_time": "Every Tuesday and Thursday 2:00-4:00 PM",
                "location": "Room 404",
                "advisor": "Mr. Shakespeare",
                "members": 21,
                "category": "Arts"
            },
            "robotics": {
                "name": "Robotics Club",
                "description": "For people who really like building robots :) ",
                "meeting_time": "Every monday 3:30-5:30 PM",
                "location": "Computer Lab",
                "advisor": "Ms. Onofre",
                "members": 23,
                "category": "Academic"
            },
            "science": {
                "name": "Science Club",
                "description": "For people who are very interested in science :)",
                "meeting_time": "Every Thursday 2:30-4:00 PM",
                "location": "Room 314",
                "advisor": "Ms. Curie",
                "members": 22,
                "category": "Academic"
            },
            "art": {
                "name": "Art Club",
                "description": "For people who really like Art :) ",
                "meeting_time": "Every Friday 1:45-4:15 PM",
                "location": "Art Room",
                "advisor": "Mr. Sava",
                "members": 24,
                "category": "Arts"
            },
             "dance": {
                "name": "Dance Club",
                "description": "For people who really like dancing :) ",
                "meeting_time": "Every Tuesday 2:45-5:30 PM",
                "location": "Music Room",
                "advisor": "Ms. Pavlova",
                "members": 24,
                "category": "Arts"
            },
            "": {
                "name": "",
                "description": "",
                "meeting_time": "",
                "location": "",
                "advisor": "",
                "members": "",
                "category": ""
            }
        }
        
def show_club_info(e):
    document.getElementById('club-info').innerHTML = " "
    selected_club = document.getElementById("club-select").value
    info = club_info.get(selected_club, club_info[""])
            
    output = f"""
            {info['name']}
            Description:{info['description']}
            Meeting Time: {info['meeting_time']}
            Location: {info['location']}
            Advisor: {info['advisor']}
            Number of Members: {info['members']}
            Category: {info['category']}
            """
    display(output, target="club-info")