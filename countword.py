
def dict_count(p):
    
    new_dict = {}
    for i in p:
        if i not in new_dict:
            new_dict[i] = 0
        new_dict[i] += 1
    print(new_dict)

def main():   
    p = "gakdkagfkgasfghslc hlHIHIVHI gvgwpahlcl"
    dict_count(p)


if __name__ == "__main__":
    main()