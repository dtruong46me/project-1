import sys
from datetime import datetime

class SubmissionContest:
    def __init__(self) -> None:
        self.submissions = dict()
        self.user_points = dict()
        self.queries = []

    def read_input(self):
        while True:
            line = [x for x in sys.stdin.readline().split()]

            if line[0] == '#':
                break

            user_id, problem_id, time_point, status, point = line
            
            key = (user_id, problem_id)
            submission = (time_point, status, int(point))

            if key not in self.submissions:
                self.submissions[key] = []

            self.submissions[key].append(submission)
            
            if key not in self.user_points or int(point) > self.user_points[key]:
                self.user_points[key] = int(point)

        while True:
            line = [x for x in sys.stdin.readline().split()]
            
            if line[0] == '#':
                break

            self.queries.append(line)


    # Total number of submissions
    def total_number_submissions(self) -> int:
        return sum(len(submissions) for submissions in self.submissions.values())


    # Total number of ERR submissions
    def number_error_submission(self) -> int:
        return sum(sum(1 for _, status, _ in submission if status=='ERR') for submission in self.submissions.values())


    # Total number of ERR submission of <UserID>
    def number_error_submission_of_user(self, user_id: str) -> int:
        return sum(sum(1 for _, status, _ in submission if status=='ERR') for key, submission in self.submissions.items() if key[0] == user_id)


    # Total point of <UserID>
    def total_point_of_user(self, user_id: str) -> int:
        return sum(point for key, point in self.user_points.items() if key[0] == user_id)
    

    # Number of submissions from <from_time_point> to <to_time_point>
    def number_submission_period(self, from_time_point, to_time_point) -> int:
        from_time_point = datetime.strptime(from_time_point, '%H:%M:%S')
        to_time_point = datetime.strptime(to_time_point, '%H:%M:%S')

        return sum(1 for submissions in self.submissions.values() for time_point, _, _ in submissions if from_time_point <= datetime.strptime(time_point, '%H:%M:%S') <= to_time_point)


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