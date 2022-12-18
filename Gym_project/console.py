import pdb

# importing classes 
from models.gym import Gym
from models.member import Member
from models.lesson import Lesson

# importing functions from repositories 
import repositories.gym_repository as gym_repository
import repositories.member_repository as member_repository
import repositories.lesson_repository as lesson_repository


# Members
member_1 = Member('steve', 'rogers', '04/Jul/1920')
member_repository.save(member_1)
member_2 = Member('tony', 'stark', "29/May/1970")
member_repository.save(member_2)
member_3 = Member('natasha', 'romanova', "03/Dec/1984")
member_repository.save(member_3)
all_members = [member_1, member_2, member_3]

# lessons
lesson_1 = Lesson('defence', '1200', '12/03/2022')
lesson_repository.save(lesson_1)
lesson_2 = Lesson('attack', '1500', '12/03/2022')
lesson_repository.save(lesson_2)
lesson_3 = Lesson('technical', '1800', '11/03/2022')
lesson_repository.save(lesson_3)

# Gym
gym_1 = Gym(member_1, lesson_2)
gym_repository.save(gym_1)
gym_2 = Gym(member_2, lesson_3)
gym_repository.save(gym_2)
gym_3 = Gym(member_2, lesson_1)
gym_repository.save(gym_3)























pdb.set_trace()