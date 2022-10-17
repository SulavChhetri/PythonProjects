from n_grams.main import ngramchecker

def test_main():
    sentence = "I am Sulav Thapa"
    assert ngramchecker(sentence,1)== sentence.split()
    assert ngramchecker(sentence,2)== ['I am', 'am Sulav', 'Sulav Thapa']
    assert ngramchecker(sentence,3)== ['I am Sulav', 'am Sulav Thapa']
    assert ngramchecker(sentence,4)== ['I am Sulav Thapa']
    assert ngramchecker(sentence,5)== ['I am Sulav Thapa']
    return "Passed"


if __name__ == '__main__':
    print(test_main())