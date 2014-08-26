def probability(hom_dom=2.0, het=2.0, hom_rec=2.0):
    total = hom_dom+het+hom_rec
    return (hom_dom / total * ((hom_dom - 1) / (total - 1))) + 2 * (hom_dom / total * (het / (total - 1))) + .75 * (het / total * ((het - 1) / (total - 1))) + (het / total * (hom_rec / (total - 1))) + 2 * (hom_dom / total * (hom_rec / (total - 1)))
    


if __name__ == '__main__':
    print probability(24.0, 30.0, 15.0)