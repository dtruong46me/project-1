import sys
from datetime import datetime

class SubmissionContest:
    def __init__(self) -> None:
        self.submissions = list()
        self.queries = []

    def read_input(self):
        while True:
            line = [x for x in sys.stdin.readline().split()]

            if line[0] == '#':
                break

            user_id, problem_id, time_point, status, point = line
            time_point = datetime.strptime(time_point, '%H:%M:%S')
            self.submissions.append((user_id, problem_id, time_point, status, int(point)))

        while True:
            line = [x for x in sys.stdin.readline().split()]
            
            if line[0] == '#':
                break

            self.queries.append(line)


    # Total number of submissions
    def total_number_submissions(self) -> int:
        return len(self.submissions)
    
    # Total number of ERR submissions
    def number_error_submission(self) -> int:
        return sum(1 for _, _, _, status, _ in self.submissions if status == 'ERR')

    # Total number of ERR submission of <UserID>
    def number_error_submission_of_user(self, user_id: str) -> int:
        return sum(1 for uid, _, _, status, _ in self.submissions if uid==user_id and status=='ERR')
    
    # Total point of <UserID>
    def total_point_of_user(self, user_id: str) -> int:
        user_points = {problem_id: 0 for _, problem_id, _, _, _ in self.submissions if user_id == user_id}
        for uid, problem_id, _, _, point in self.submissions:
            if uid == user_id and point > user_points[problem_id]:
                user_points[problem_id] = point
        
        return sum(user_points.values())
    
    # Number of submissions from <from_time_point> to <to_time_point>
    def number_submission_period(self, from_time_point, to_time_point) -> int:
        from_time_point = datetime.strptime(from_time_point, '%H:%M:%S')
        to_time_point = datetime.strptime(to_time_point, '%H:%M:%S')

        return sum(1 for _, _, time_point, _, _ in self.submissions if from_time_point <= time_point <= to_time_point)
    

    # Handle requests
    def handle_requests(self):
        for query in self.queries:
            if query[0] == '?total_number_submissions':
                print(self.total_number_submissions())

            if query[0] == '?number_error_submision':
                print(self.number_error_submission())

            if query[0] == '?number_error_submision_of_user':
                print(self.number_error_submission_of_user(query[1]))

            if query[0] == '?total_point_of_user':
                print(self.total_point_of_user(query[1]))

            if query[0] == '?number_submission_period':
                print(self.number_submission_period(query[1], query[2]))


def main():
    submisison_contest = SubmissionContest()
    submisison_contest.read_input()
    submisison_contest.handle_requests()


if __name__ == '__main__':
    main()