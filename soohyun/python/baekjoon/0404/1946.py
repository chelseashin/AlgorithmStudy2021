# 12t시 45분
# 끝 13시 20분
import sys
from heapq import heappush, heappop


def judge(paper_heap, interview_heap, applicants):
    done = list()
    while len(paper_heap) > 0:
        paper = heappop(paper_heap)
        interview = applicants[paper]
        while len(interview_heap) > 0:
            pass_fail = abs(heappop(interview_heap))
            if interview > pass_fail:
                heappush(interview_heap, -pass_fail)
                break
            if interview == pass_fail:
                done.append((paper, interview))
                break
    return len(done)


def main():
    T = int(sys.stdin.readline().rstrip())
    for _ in range(T):
        N = int(sys.stdin.readline().rstrip())
        paper_heap = list()
        interview_heap = list()
        applicants = dict()
        done = list()
        for _ in range(N):
            paper, interview = map(int,
                            sys.stdin.readline().rstrip().split(" "))
            heappush(paper_heap, paper)
            heappush(interview_heap, -interview)
            applicants[paper] = interview
        done = judge(paper_heap, interview_heap, applicants)
        print(done)


if __name__ == "__main__":
    main()