def f1(precision, recall):
    return 2*(precision*recall)/(precision+recall)


if __name__ == '__main__':
    # Matrix for crypto finance
    TP = 70  # on how many days did you correctly predict the market goes up?
    FP = 10  # on how many days did you predict the market goes up, but it actually went down?
    FN = 8   # on how many days did you predict the market goes down, but it actually went up?
    TN = 12  # on how many days did you correctly predict the market goes down?

    precision = TP / (TP + FP)
    print("When it predicts a positive move up it's correct {p}% of the time".format(p=100*precision))
    recall = TP / (TP + FN)
    print("It correctly identifies the fraction {p}% of positive days".format(p=100*recall))
    print("The F1 measure: {f}".format(f=f1(precision=precision, recall=recall)))

    # Matrix for BTC
    TP = 80  # the number of days BTC went up
    FP = 20  # the number of days BTC went down
    FN = 0   # we never predict the market goes down
    TN = 0   # we never predict the market goes down

    precision = TP / (TP + FP)
    print("When it predicts a positive move up it's correct {p}% of the time".format(p=100*precision))
    recall = TP / (TP + FN)
    print("It correctly identifies the fraction {p}% of positive days".format(p=100*recall))
    print("The F1 measure: {f}".format(f=f1(precision=precision, recall=recall)))
