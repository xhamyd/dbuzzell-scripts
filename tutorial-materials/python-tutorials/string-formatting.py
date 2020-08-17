def main():
    name = "David"
    score = 7
    print("Name: %s" % (name,))
    print("Total score of %s is %s" % (name, score))
    print("Total score of %(n)s is %(s)s" % {'n': name, 's':score})
    print("Total score for {} is {}".format(name, score))
    print("Total score for {0} is {1}".format(name, score))
    print("Total score for {n} is {s}".format(n=name, s=score))
    print("Total score for " + str(name) + " is " + str(score))
    print(f'Total score for {name} is {score}')  # only in Python 3.6

    # Need 'from __future__ import print_function' if in Python 2
    print("Total score for", name, "is", score)
    print("Total score for ", name, " is ", score, sep='')


if __name__ == "__main__":
    main()
