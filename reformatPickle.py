#take the 20 np arrays in each pickle file and add them to a list so they are iterable

import netCDF4 as nc
import numpy as np
from matplotlib import pyplot as plt
import pickle
import os

titles = ["fm100", "pet", "pr", "sph", "srad", "th", "tmmn", "tmmx", "vs"]
for title in titles:
    fn = "data/pickle_old/" + title + ".pickle"
    newfn = "data/pickle/" + title + ".pickle"

    a2000 = pickle.load(open(fn, "rb"))
    b2001 = pickle.load(open(fn, "rb"))
    c2002 = pickle.load(open(fn, "rb"))
    d2003 = pickle.load(open(fn, "rb"))
    e2004 = pickle.load(open(fn, "rb"))
    f2005 = pickle.load(open(fn, "rb"))
    g2006 = pickle.load(open(fn, "rb"))
    h2007 = pickle.load(open(fn, "rb"))
    i2008 = pickle.load(open(fn, "rb"))
    j2009 = pickle.load(open(fn, "rb"))
    k2010 = pickle.load(open(fn, "rb"))
    l2011 = pickle.load(open(fn, "rb"))
    m2012 = pickle.load(open(fn, "rb"))
    n2013 = pickle.load(open(fn, "rb"))
    o2014 = pickle.load(open(fn, "rb"))
    p2015 = pickle.load(open(fn, "rb"))
    q2016 = pickle.load(open(fn, "rb"))
    r2017 = pickle.load(open(fn, "rb"))
    s2018 = pickle.load(open(fn, "rb"))
    t2019 = pickle.load(open(fn, "rb"))
    u2020 = pickle.load(open(fn, "rb"))

    Array = [a2000, b2001, c2002, d2003, e2004, f2005, g2006, h2007, i2008, j2009, k2010, l2011, m2012, n2013, o2014, p2015, q2016, r2017, s2018, t2019, u2020]

    pickle.dump( Array, open( newfn, "wb" ) )
    print("put in pickle:", title)
