def kerro3(ika):
    if ika < 13:
        tulos = "child"
    elif ika < 20:
        tulos = "teen"
    elif ika < 66:
        tulos = "adult"
    else:
        tulos = "senior"
    return tulos