import pdb

# importing classes 
from models.booking import Booking
from models.member import Member
from models.lesson import Lesson

# importing functions from repositories 
import repositories.booking_repository as booking_repository
import repositories.member_repository as member_repository
import repositories.lesson_repository as lesson_repository


# Members
member_1 = Member('steve', 'rogers', '04/Jul/1920')
member_repository.save(member_1)
member_2 = Member('tony', 'stark', "29/May/1970")
member_repository.save(member_2)
member_3 = Member('natasha', 'romanova', "03/Dec/1984")
member_repository.save(member_3)


# lessons
lesson_1 = Lesson('defence', '1200', '12/03/2022')
lesson_repository.save(lesson_1)
lesson_2 = Lesson('attack', '1500', '12/03/2022')
lesson_repository.save(lesson_2)
lesson_3 = Lesson('technical', '1800', '11/03/2022')
lesson_repository.save(lesson_3)

# Gym
booking_1 = Booking(member_1, lesson_2)
booking_repository.save(booking_1)
booking_2 = Booking(member_2, lesson_3)
booking_repository.save(booking_2)
booking_3 = Booking(member_2, lesson_1)
booking_repository.save(booking_3)
booking_4 = Booking(member_3, lesson_3)
booking_repository.save(booking_4)























pdb.set_trace()