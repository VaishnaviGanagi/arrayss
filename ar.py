def main():
    scores=[33,44,55,66,89]
    total=sum(scores)
    average=total/len(scores)
    print(f"scores:{scores}")
    print(f"sum:{total}")
    print(f"average:{average}")
    print(f"Maximum:{max(scores)}")
    print(f"Minimum:{min(scores)}")
if __name__=="__main__":
    main()