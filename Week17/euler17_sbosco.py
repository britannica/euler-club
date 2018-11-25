# euler17
import time
    
def onedigit(num):
    if num == 1:
        return 'one'
    elif num == 2:
        return 'two'
    elif num == 3:
        return 'three'
    elif num == 4:
        return 'four'
    elif num == 5:
        return 'five'
    elif num == 6:
        return 'six'
    elif num == 7:
        return 'seven'
    elif num == 8:
        return 'eight'
    elif num == 9:
        return 'nine'
    return

def twodigits(num):
    onesdigit = num % 10
    if num < 10:
        return onedigit(onesdigit)
    if num == 10:
        return 'ten'
    elif num == 11:
        return 'eleven'
    elif num == 12:
        return 'twelve'
    elif num == 13:
        return 'thirteen'
    elif num == 14:
        return 'fourteen'
    elif num == 15:
        return 'fifteen'
    elif num == 16:
        return 'sixteen'
    elif num == 17:
        return 'seventeen'
    elif num == 18:
        return 'eighteen'
    elif num == 19:
        return 'nineteen'
    if num < 10:
        words = 'twenty'
    elif num < 30:
        words = 'twenty'
    elif num < 40:
        words = 'thirty'
    elif num < 50:
        words = 'forty'
    elif num < 60:
        words = 'fifty'
    elif num < 70:
        words = 'sixty'
    elif num < 80:
        words = 'seventy'
    elif num < 90:
        words = 'eighty'
    elif num < 100:
        words = 'ninety'
    if onesdigit == 0:
        return words
    onesword = onedigit(onesdigit)
    words = words + '-' + onesword
    return words

def threedigits(num):
    digit1 = int(str(num)[0])
    words = onedigit(digit1) + ' hundred'
    digit2_3 = int(str(num)[1:3])
    words2_3 = twodigits(digit2_3)
    if words2_3:
        words = words + ' and ' + words2_3
    return words
    
def wordlength(words):
    words = words.replace('-', '')
    words = words.replace(' ', '')
    return len(words)

t0 = time.time()
totalletters = 0
for num in range(1,1001):
    if num < 10:
        words = onedigit(num)
    elif num < 100:
        words = twodigits(num)
    elif num < 1000:
        words = threedigits(num)
    if num == 1000:
        words = 'one thousand'
    chars = wordlength(words)
    print(num, words, chars)
    totalletters += chars
print('total letters = ',totalletters)


t1 = time.time()
elapsed = t1 - t0
print('time=',elapsed)


###################### OUTPUT #######################
1 one 3
2 two 3
3 three 5
4 four 4
5 five 4
6 six 3
7 seven 5
8 eight 5
9 nine 4
10 ten 3
11 eleven 6
12 twelve 6
13 thirteen 8
14 fourteen 8
15 fifteen 7
16 sixteen 7
17 seventeen 9
18 eighteen 8
19 nineteen 8
20 twenty 6
21 twenty-one 9
22 twenty-two 9
23 twenty-three 11
24 twenty-four 10
25 twenty-five 10
26 twenty-six 9
27 twenty-seven 11
28 twenty-eight 11
29 twenty-nine 10
30 thirty 6
31 thirty-one 9
32 thirty-two 9
33 thirty-three 11
34 thirty-four 10
35 thirty-five 10
36 thirty-six 9
37 thirty-seven 11
38 thirty-eight 11
39 thirty-nine 10
40 forty 5
41 forty-one 8
42 forty-two 8
43 forty-three 10
44 forty-four 9
45 forty-five 9
46 forty-six 8
47 forty-seven 10
48 forty-eight 10
49 forty-nine 9
50 fifty 5
51 fifty-one 8
52 fifty-two 8
53 fifty-three 10
54 fifty-four 9
55 fifty-five 9
56 fifty-six 8
57 fifty-seven 10
58 fifty-eight 10
59 fifty-nine 9
60 sixty 5
61 sixty-one 8
62 sixty-two 8
63 sixty-three 10
64 sixty-four 9
65 sixty-five 9
66 sixty-six 8
67 sixty-seven 10
68 sixty-eight 10
69 sixty-nine 9
70 seventy 7
71 seventy-one 10
72 seventy-two 10
73 seventy-three 12
74 seventy-four 11
75 seventy-five 11
76 seventy-six 10
77 seventy-seven 12
78 seventy-eight 12
79 seventy-nine 11
80 eighty 6
81 eighty-one 9
82 eighty-two 9
83 eighty-three 11
84 eighty-four 10
85 eighty-five 10
86 eighty-six 9
87 eighty-seven 11
88 eighty-eight 11
89 eighty-nine 10
90 ninety 6
91 ninety-one 9
92 ninety-two 9
93 ninety-three 11
94 ninety-four 10
95 ninety-five 10
96 ninety-six 9
97 ninety-seven 11
98 ninety-eight 11
99 ninety-nine 10
100 one hundred 10
101 one hundred and one 16
102 one hundred and two 16
103 one hundred and three 18
104 one hundred and four 17
105 one hundred and five 17
106 one hundred and six 16
107 one hundred and seven 18
108 one hundred and eight 18
109 one hundred and nine 17
110 one hundred and ten 16
111 one hundred and eleven 19
112 one hundred and twelve 19
113 one hundred and thirteen 21
114 one hundred and fourteen 21
115 one hundred and fifteen 20
116 one hundred and sixteen 20
117 one hundred and seventeen 22
118 one hundred and eighteen 21
119 one hundred and nineteen 21
120 one hundred and twenty 19
121 one hundred and twenty-one 22
122 one hundred and twenty-two 22
123 one hundred and twenty-three 24
124 one hundred and twenty-four 23
125 one hundred and twenty-five 23
126 one hundred and twenty-six 22
127 one hundred and twenty-seven 24
128 one hundred and twenty-eight 24
129 one hundred and twenty-nine 23
130 one hundred and thirty 19
131 one hundred and thirty-one 22
132 one hundred and thirty-two 22
133 one hundred and thirty-three 24
134 one hundred and thirty-four 23
135 one hundred and thirty-five 23
136 one hundred and thirty-six 22
137 one hundred and thirty-seven 24
138 one hundred and thirty-eight 24
139 one hundred and thirty-nine 23
140 one hundred and forty 18
141 one hundred and forty-one 21
142 one hundred and forty-two 21
143 one hundred and forty-three 23
144 one hundred and forty-four 22
145 one hundred and forty-five 22
146 one hundred and forty-six 21
147 one hundred and forty-seven 23
148 one hundred and forty-eight 23
149 one hundred and forty-nine 22
150 one hundred and fifty 18
151 one hundred and fifty-one 21
152 one hundred and fifty-two 21
153 one hundred and fifty-three 23
154 one hundred and fifty-four 22
155 one hundred and fifty-five 22
156 one hundred and fifty-six 21
157 one hundred and fifty-seven 23
158 one hundred and fifty-eight 23
159 one hundred and fifty-nine 22
160 one hundred and sixty 18
161 one hundred and sixty-one 21
162 one hundred and sixty-two 21
163 one hundred and sixty-three 23
164 one hundred and sixty-four 22
165 one hundred and sixty-five 22
166 one hundred and sixty-six 21
167 one hundred and sixty-seven 23
168 one hundred and sixty-eight 23
169 one hundred and sixty-nine 22
170 one hundred and seventy 20
171 one hundred and seventy-one 23
172 one hundred and seventy-two 23
173 one hundred and seventy-three 25
174 one hundred and seventy-four 24
175 one hundred and seventy-five 24
176 one hundred and seventy-six 23
177 one hundred and seventy-seven 25
178 one hundred and seventy-eight 25
179 one hundred and seventy-nine 24
180 one hundred and eighty 19
181 one hundred and eighty-one 22
182 one hundred and eighty-two 22
183 one hundred and eighty-three 24
184 one hundred and eighty-four 23
185 one hundred and eighty-five 23
186 one hundred and eighty-six 22
187 one hundred and eighty-seven 24
188 one hundred and eighty-eight 24
189 one hundred and eighty-nine 23
190 one hundred and ninety 19
191 one hundred and ninety-one 22
192 one hundred and ninety-two 22
193 one hundred and ninety-three 24
194 one hundred and ninety-four 23
195 one hundred and ninety-five 23
196 one hundred and ninety-six 22
197 one hundred and ninety-seven 24
198 one hundred and ninety-eight 24
199 one hundred and ninety-nine 23
200 two hundred 10
201 two hundred and one 16
202 two hundred and two 16
203 two hundred and three 18
204 two hundred and four 17
205 two hundred and five 17
206 two hundred and six 16
207 two hundred and seven 18
208 two hundred and eight 18
209 two hundred and nine 17
210 two hundred and ten 16
211 two hundred and eleven 19
212 two hundred and twelve 19
213 two hundred and thirteen 21
214 two hundred and fourteen 21
215 two hundred and fifteen 20
216 two hundred and sixteen 20
217 two hundred and seventeen 22
218 two hundred and eighteen 21
219 two hundred and nineteen 21
220 two hundred and twenty 19
221 two hundred and twenty-one 22
222 two hundred and twenty-two 22
223 two hundred and twenty-three 24
224 two hundred and twenty-four 23
225 two hundred and twenty-five 23
226 two hundred and twenty-six 22
227 two hundred and twenty-seven 24
228 two hundred and twenty-eight 24
229 two hundred and twenty-nine 23
230 two hundred and thirty 19
231 two hundred and thirty-one 22
232 two hundred and thirty-two 22
233 two hundred and thirty-three 24
234 two hundred and thirty-four 23
235 two hundred and thirty-five 23
236 two hundred and thirty-six 22
237 two hundred and thirty-seven 24
238 two hundred and thirty-eight 24
239 two hundred and thirty-nine 23
240 two hundred and forty 18
241 two hundred and forty-one 21
242 two hundred and forty-two 21
243 two hundred and forty-three 23
244 two hundred and forty-four 22
245 two hundred and forty-five 22
246 two hundred and forty-six 21
247 two hundred and forty-seven 23
248 two hundred and forty-eight 23
249 two hundred and forty-nine 22
250 two hundred and fifty 18
251 two hundred and fifty-one 21
252 two hundred and fifty-two 21
253 two hundred and fifty-three 23
254 two hundred and fifty-four 22
255 two hundred and fifty-five 22
256 two hundred and fifty-six 21
257 two hundred and fifty-seven 23
258 two hundred and fifty-eight 23
259 two hundred and fifty-nine 22
260 two hundred and sixty 18
261 two hundred and sixty-one 21
262 two hundred and sixty-two 21
263 two hundred and sixty-three 23
264 two hundred and sixty-four 22
265 two hundred and sixty-five 22
266 two hundred and sixty-six 21
267 two hundred and sixty-seven 23
268 two hundred and sixty-eight 23
269 two hundred and sixty-nine 22
270 two hundred and seventy 20
271 two hundred and seventy-one 23
272 two hundred and seventy-two 23
273 two hundred and seventy-three 25
274 two hundred and seventy-four 24
275 two hundred and seventy-five 24
276 two hundred and seventy-six 23
277 two hundred and seventy-seven 25
278 two hundred and seventy-eight 25
279 two hundred and seventy-nine 24
280 two hundred and eighty 19
281 two hundred and eighty-one 22
282 two hundred and eighty-two 22
283 two hundred and eighty-three 24
284 two hundred and eighty-four 23
285 two hundred and eighty-five 23
286 two hundred and eighty-six 22
287 two hundred and eighty-seven 24
288 two hundred and eighty-eight 24
289 two hundred and eighty-nine 23
290 two hundred and ninety 19
291 two hundred and ninety-one 22
292 two hundred and ninety-two 22
293 two hundred and ninety-three 24
294 two hundred and ninety-four 23
295 two hundred and ninety-five 23
296 two hundred and ninety-six 22
297 two hundred and ninety-seven 24
298 two hundred and ninety-eight 24
299 two hundred and ninety-nine 23
300 three hundred 12
301 three hundred and one 18
302 three hundred and two 18
303 three hundred and three 20
304 three hundred and four 19
305 three hundred and five 19
306 three hundred and six 18
307 three hundred and seven 20
308 three hundred and eight 20
309 three hundred and nine 19
310 three hundred and ten 18
311 three hundred and eleven 21
312 three hundred and twelve 21
313 three hundred and thirteen 23
314 three hundred and fourteen 23
315 three hundred and fifteen 22
316 three hundred and sixteen 22
317 three hundred and seventeen 24
318 three hundred and eighteen 23
319 three hundred and nineteen 23
320 three hundred and twenty 21
321 three hundred and twenty-one 24
322 three hundred and twenty-two 24
323 three hundred and twenty-three 26
324 three hundred and twenty-four 25
325 three hundred and twenty-five 25
326 three hundred and twenty-six 24
327 three hundred and twenty-seven 26
328 three hundred and twenty-eight 26
329 three hundred and twenty-nine 25
330 three hundred and thirty 21
331 three hundred and thirty-one 24
332 three hundred and thirty-two 24
333 three hundred and thirty-three 26
334 three hundred and thirty-four 25
335 three hundred and thirty-five 25
336 three hundred and thirty-six 24
337 three hundred and thirty-seven 26
338 three hundred and thirty-eight 26
339 three hundred and thirty-nine 25
340 three hundred and forty 20
341 three hundred and forty-one 23
342 three hundred and forty-two 23
343 three hundred and forty-three 25
344 three hundred and forty-four 24
345 three hundred and forty-five 24
346 three hundred and forty-six 23
347 three hundred and forty-seven 25
348 three hundred and forty-eight 25
349 three hundred and forty-nine 24
350 three hundred and fifty 20
351 three hundred and fifty-one 23
352 three hundred and fifty-two 23
353 three hundred and fifty-three 25
354 three hundred and fifty-four 24
355 three hundred and fifty-five 24
356 three hundred and fifty-six 23
357 three hundred and fifty-seven 25
358 three hundred and fifty-eight 25
359 three hundred and fifty-nine 24
360 three hundred and sixty 20
361 three hundred and sixty-one 23
362 three hundred and sixty-two 23
363 three hundred and sixty-three 25
364 three hundred and sixty-four 24
365 three hundred and sixty-five 24
366 three hundred and sixty-six 23
367 three hundred and sixty-seven 25
368 three hundred and sixty-eight 25
369 three hundred and sixty-nine 24
370 three hundred and seventy 22
371 three hundred and seventy-one 25
372 three hundred and seventy-two 25
373 three hundred and seventy-three 27
374 three hundred and seventy-four 26
375 three hundred and seventy-five 26
376 three hundred and seventy-six 25
377 three hundred and seventy-seven 27
378 three hundred and seventy-eight 27
379 three hundred and seventy-nine 26
380 three hundred and eighty 21
381 three hundred and eighty-one 24
382 three hundred and eighty-two 24
383 three hundred and eighty-three 26
384 three hundred and eighty-four 25
385 three hundred and eighty-five 25
386 three hundred and eighty-six 24
387 three hundred and eighty-seven 26
388 three hundred and eighty-eight 26
389 three hundred and eighty-nine 25
390 three hundred and ninety 21
391 three hundred and ninety-one 24
392 three hundred and ninety-two 24
393 three hundred and ninety-three 26
394 three hundred and ninety-four 25
395 three hundred and ninety-five 25
396 three hundred and ninety-six 24
397 three hundred and ninety-seven 26
398 three hundred and ninety-eight 26
399 three hundred and ninety-nine 25
400 four hundred 11
401 four hundred and one 17
402 four hundred and two 17
403 four hundred and three 19
404 four hundred and four 18
405 four hundred and five 18
406 four hundred and six 17
407 four hundred and seven 19
408 four hundred and eight 19
409 four hundred and nine 18
410 four hundred and ten 17
411 four hundred and eleven 20
412 four hundred and twelve 20
413 four hundred and thirteen 22
414 four hundred and fourteen 22
415 four hundred and fifteen 21
416 four hundred and sixteen 21
417 four hundred and seventeen 23
418 four hundred and eighteen 22
419 four hundred and nineteen 22
420 four hundred and twenty 20
421 four hundred and twenty-one 23
422 four hundred and twenty-two 23
423 four hundred and twenty-three 25
424 four hundred and twenty-four 24
425 four hundred and twenty-five 24
426 four hundred and twenty-six 23
427 four hundred and twenty-seven 25
428 four hundred and twenty-eight 25
429 four hundred and twenty-nine 24
430 four hundred and thirty 20
431 four hundred and thirty-one 23
432 four hundred and thirty-two 23
433 four hundred and thirty-three 25
434 four hundred and thirty-four 24
435 four hundred and thirty-five 24
436 four hundred and thirty-six 23
437 four hundred and thirty-seven 25
438 four hundred and thirty-eight 25
439 four hundred and thirty-nine 24
440 four hundred and forty 19
441 four hundred and forty-one 22
442 four hundred and forty-two 22
443 four hundred and forty-three 24
444 four hundred and forty-four 23
445 four hundred and forty-five 23
446 four hundred and forty-six 22
447 four hundred and forty-seven 24
448 four hundred and forty-eight 24
449 four hundred and forty-nine 23
450 four hundred and fifty 19
451 four hundred and fifty-one 22
452 four hundred and fifty-two 22
453 four hundred and fifty-three 24
454 four hundred and fifty-four 23
455 four hundred and fifty-five 23
456 four hundred and fifty-six 22
457 four hundred and fifty-seven 24
458 four hundred and fifty-eight 24
459 four hundred and fifty-nine 23
460 four hundred and sixty 19
461 four hundred and sixty-one 22
462 four hundred and sixty-two 22
463 four hundred and sixty-three 24
464 four hundred and sixty-four 23
465 four hundred and sixty-five 23
466 four hundred and sixty-six 22
467 four hundred and sixty-seven 24
468 four hundred and sixty-eight 24
469 four hundred and sixty-nine 23
470 four hundred and seventy 21
471 four hundred and seventy-one 24
472 four hundred and seventy-two 24
473 four hundred and seventy-three 26
474 four hundred and seventy-four 25
475 four hundred and seventy-five 25
476 four hundred and seventy-six 24
477 four hundred and seventy-seven 26
478 four hundred and seventy-eight 26
479 four hundred and seventy-nine 25
480 four hundred and eighty 20
481 four hundred and eighty-one 23
482 four hundred and eighty-two 23
483 four hundred and eighty-three 25
484 four hundred and eighty-four 24
485 four hundred and eighty-five 24
486 four hundred and eighty-six 23
487 four hundred and eighty-seven 25
488 four hundred and eighty-eight 25
489 four hundred and eighty-nine 24
490 four hundred and ninety 20
491 four hundred and ninety-one 23
492 four hundred and ninety-two 23
493 four hundred and ninety-three 25
494 four hundred and ninety-four 24
495 four hundred and ninety-five 24
496 four hundred and ninety-six 23
497 four hundred and ninety-seven 25
498 four hundred and ninety-eight 25
499 four hundred and ninety-nine 24
500 five hundred 11
501 five hundred and one 17
502 five hundred and two 17
503 five hundred and three 19
504 five hundred and four 18
505 five hundred and five 18
506 five hundred and six 17
507 five hundred and seven 19
508 five hundred and eight 19
509 five hundred and nine 18
510 five hundred and ten 17
511 five hundred and eleven 20
512 five hundred and twelve 20
513 five hundred and thirteen 22
514 five hundred and fourteen 22
515 five hundred and fifteen 21
516 five hundred and sixteen 21
517 five hundred and seventeen 23
518 five hundred and eighteen 22
519 five hundred and nineteen 22
520 five hundred and twenty 20
521 five hundred and twenty-one 23
522 five hundred and twenty-two 23
523 five hundred and twenty-three 25
524 five hundred and twenty-four 24
525 five hundred and twenty-five 24
526 five hundred and twenty-six 23
527 five hundred and twenty-seven 25
528 five hundred and twenty-eight 25
529 five hundred and twenty-nine 24
530 five hundred and thirty 20
531 five hundred and thirty-one 23
532 five hundred and thirty-two 23
533 five hundred and thirty-three 25
534 five hundred and thirty-four 24
535 five hundred and thirty-five 24
536 five hundred and thirty-six 23
537 five hundred and thirty-seven 25
538 five hundred and thirty-eight 25
539 five hundred and thirty-nine 24
540 five hundred and forty 19
541 five hundred and forty-one 22
542 five hundred and forty-two 22
543 five hundred and forty-three 24
544 five hundred and forty-four 23
545 five hundred and forty-five 23
546 five hundred and forty-six 22
547 five hundred and forty-seven 24
548 five hundred and forty-eight 24
549 five hundred and forty-nine 23
550 five hundred and fifty 19
551 five hundred and fifty-one 22
552 five hundred and fifty-two 22
553 five hundred and fifty-three 24
554 five hundred and fifty-four 23
555 five hundred and fifty-five 23
556 five hundred and fifty-six 22
557 five hundred and fifty-seven 24
558 five hundred and fifty-eight 24
559 five hundred and fifty-nine 23
560 five hundred and sixty 19
561 five hundred and sixty-one 22
562 five hundred and sixty-two 22
563 five hundred and sixty-three 24
564 five hundred and sixty-four 23
565 five hundred and sixty-five 23
566 five hundred and sixty-six 22
567 five hundred and sixty-seven 24
568 five hundred and sixty-eight 24
569 five hundred and sixty-nine 23
570 five hundred and seventy 21
571 five hundred and seventy-one 24
572 five hundred and seventy-two 24
573 five hundred and seventy-three 26
574 five hundred and seventy-four 25
575 five hundred and seventy-five 25
576 five hundred and seventy-six 24
577 five hundred and seventy-seven 26
578 five hundred and seventy-eight 26
579 five hundred and seventy-nine 25
580 five hundred and eighty 20
581 five hundred and eighty-one 23
582 five hundred and eighty-two 23
583 five hundred and eighty-three 25
584 five hundred and eighty-four 24
585 five hundred and eighty-five 24
586 five hundred and eighty-six 23
587 five hundred and eighty-seven 25
588 five hundred and eighty-eight 25
589 five hundred and eighty-nine 24
590 five hundred and ninety 20
591 five hundred and ninety-one 23
592 five hundred and ninety-two 23
593 five hundred and ninety-three 25
594 five hundred and ninety-four 24
595 five hundred and ninety-five 24
596 five hundred and ninety-six 23
597 five hundred and ninety-seven 25
598 five hundred and ninety-eight 25
599 five hundred and ninety-nine 24
600 six hundred 10
601 six hundred and one 16
602 six hundred and two 16
603 six hundred and three 18
604 six hundred and four 17
605 six hundred and five 17
606 six hundred and six 16
607 six hundred and seven 18
608 six hundred and eight 18
609 six hundred and nine 17
610 six hundred and ten 16
611 six hundred and eleven 19
612 six hundred and twelve 19
613 six hundred and thirteen 21
614 six hundred and fourteen 21
615 six hundred and fifteen 20
616 six hundred and sixteen 20
617 six hundred and seventeen 22
618 six hundred and eighteen 21
619 six hundred and nineteen 21
620 six hundred and twenty 19
621 six hundred and twenty-one 22
622 six hundred and twenty-two 22
623 six hundred and twenty-three 24
624 six hundred and twenty-four 23
625 six hundred and twenty-five 23
626 six hundred and twenty-six 22
627 six hundred and twenty-seven 24
628 six hundred and twenty-eight 24
629 six hundred and twenty-nine 23
630 six hundred and thirty 19
631 six hundred and thirty-one 22
632 six hundred and thirty-two 22
633 six hundred and thirty-three 24
634 six hundred and thirty-four 23
635 six hundred and thirty-five 23
636 six hundred and thirty-six 22
637 six hundred and thirty-seven 24
638 six hundred and thirty-eight 24
639 six hundred and thirty-nine 23
640 six hundred and forty 18
641 six hundred and forty-one 21
642 six hundred and forty-two 21
643 six hundred and forty-three 23
644 six hundred and forty-four 22
645 six hundred and forty-five 22
646 six hundred and forty-six 21
647 six hundred and forty-seven 23
648 six hundred and forty-eight 23
649 six hundred and forty-nine 22
650 six hundred and fifty 18
651 six hundred and fifty-one 21
652 six hundred and fifty-two 21
653 six hundred and fifty-three 23
654 six hundred and fifty-four 22
655 six hundred and fifty-five 22
656 six hundred and fifty-six 21
657 six hundred and fifty-seven 23
658 six hundred and fifty-eight 23
659 six hundred and fifty-nine 22
660 six hundred and sixty 18
661 six hundred and sixty-one 21
662 six hundred and sixty-two 21
663 six hundred and sixty-three 23
664 six hundred and sixty-four 22
665 six hundred and sixty-five 22
666 six hundred and sixty-six 21
667 six hundred and sixty-seven 23
668 six hundred and sixty-eight 23
669 six hundred and sixty-nine 22
670 six hundred and seventy 20
671 six hundred and seventy-one 23
672 six hundred and seventy-two 23
673 six hundred and seventy-three 25
674 six hundred and seventy-four 24
675 six hundred and seventy-five 24
676 six hundred and seventy-six 23
677 six hundred and seventy-seven 25
678 six hundred and seventy-eight 25
679 six hundred and seventy-nine 24
680 six hundred and eighty 19
681 six hundred and eighty-one 22
682 six hundred and eighty-two 22
683 six hundred and eighty-three 24
684 six hundred and eighty-four 23
685 six hundred and eighty-five 23
686 six hundred and eighty-six 22
687 six hundred and eighty-seven 24
688 six hundred and eighty-eight 24
689 six hundred and eighty-nine 23
690 six hundred and ninety 19
691 six hundred and ninety-one 22
692 six hundred and ninety-two 22
693 six hundred and ninety-three 24
694 six hundred and ninety-four 23
695 six hundred and ninety-five 23
696 six hundred and ninety-six 22
697 six hundred and ninety-seven 24
698 six hundred and ninety-eight 24
699 six hundred and ninety-nine 23
700 seven hundred 12
701 seven hundred and one 18
702 seven hundred and two 18
703 seven hundred and three 20
704 seven hundred and four 19
705 seven hundred and five 19
706 seven hundred and six 18
707 seven hundred and seven 20
708 seven hundred and eight 20
709 seven hundred and nine 19
710 seven hundred and ten 18
711 seven hundred and eleven 21
712 seven hundred and twelve 21
713 seven hundred and thirteen 23
714 seven hundred and fourteen 23
715 seven hundred and fifteen 22
716 seven hundred and sixteen 22
717 seven hundred and seventeen 24
718 seven hundred and eighteen 23
719 seven hundred and nineteen 23
720 seven hundred and twenty 21
721 seven hundred and twenty-one 24
722 seven hundred and twenty-two 24
723 seven hundred and twenty-three 26
724 seven hundred and twenty-four 25
725 seven hundred and twenty-five 25
726 seven hundred and twenty-six 24
727 seven hundred and twenty-seven 26
728 seven hundred and twenty-eight 26
729 seven hundred and twenty-nine 25
730 seven hundred and thirty 21
731 seven hundred and thirty-one 24
732 seven hundred and thirty-two 24
733 seven hundred and thirty-three 26
734 seven hundred and thirty-four 25
735 seven hundred and thirty-five 25
736 seven hundred and thirty-six 24
737 seven hundred and thirty-seven 26
738 seven hundred and thirty-eight 26
739 seven hundred and thirty-nine 25
740 seven hundred and forty 20
741 seven hundred and forty-one 23
742 seven hundred and forty-two 23
743 seven hundred and forty-three 25
744 seven hundred and forty-four 24
745 seven hundred and forty-five 24
746 seven hundred and forty-six 23
747 seven hundred and forty-seven 25
748 seven hundred and forty-eight 25
749 seven hundred and forty-nine 24
750 seven hundred and fifty 20
751 seven hundred and fifty-one 23
752 seven hundred and fifty-two 23
753 seven hundred and fifty-three 25
754 seven hundred and fifty-four 24
755 seven hundred and fifty-five 24
756 seven hundred and fifty-six 23
757 seven hundred and fifty-seven 25
758 seven hundred and fifty-eight 25
759 seven hundred and fifty-nine 24
760 seven hundred and sixty 20
761 seven hundred and sixty-one 23
762 seven hundred and sixty-two 23
763 seven hundred and sixty-three 25
764 seven hundred and sixty-four 24
765 seven hundred and sixty-five 24
766 seven hundred and sixty-six 23
767 seven hundred and sixty-seven 25
768 seven hundred and sixty-eight 25
769 seven hundred and sixty-nine 24
770 seven hundred and seventy 22
771 seven hundred and seventy-one 25
772 seven hundred and seventy-two 25
773 seven hundred and seventy-three 27
774 seven hundred and seventy-four 26
775 seven hundred and seventy-five 26
776 seven hundred and seventy-six 25
777 seven hundred and seventy-seven 27
778 seven hundred and seventy-eight 27
779 seven hundred and seventy-nine 26
780 seven hundred and eighty 21
781 seven hundred and eighty-one 24
782 seven hundred and eighty-two 24
783 seven hundred and eighty-three 26
784 seven hundred and eighty-four 25
785 seven hundred and eighty-five 25
786 seven hundred and eighty-six 24
787 seven hundred and eighty-seven 26
788 seven hundred and eighty-eight 26
789 seven hundred and eighty-nine 25
790 seven hundred and ninety 21
791 seven hundred and ninety-one 24
792 seven hundred and ninety-two 24
793 seven hundred and ninety-three 26
794 seven hundred and ninety-four 25
795 seven hundred and ninety-five 25
796 seven hundred and ninety-six 24
797 seven hundred and ninety-seven 26
798 seven hundred and ninety-eight 26
799 seven hundred and ninety-nine 25
800 eight hundred 12
801 eight hundred and one 18
802 eight hundred and two 18
803 eight hundred and three 20
804 eight hundred and four 19
805 eight hundred and five 19
806 eight hundred and six 18
807 eight hundred and seven 20
808 eight hundred and eight 20
809 eight hundred and nine 19
810 eight hundred and ten 18
811 eight hundred and eleven 21
812 eight hundred and twelve 21
813 eight hundred and thirteen 23
814 eight hundred and fourteen 23
815 eight hundred and fifteen 22
816 eight hundred and sixteen 22
817 eight hundred and seventeen 24
818 eight hundred and eighteen 23
819 eight hundred and nineteen 23
820 eight hundred and twenty 21
821 eight hundred and twenty-one 24
822 eight hundred and twenty-two 24
823 eight hundred and twenty-three 26
824 eight hundred and twenty-four 25
825 eight hundred and twenty-five 25
826 eight hundred and twenty-six 24
827 eight hundred and twenty-seven 26
828 eight hundred and twenty-eight 26
829 eight hundred and twenty-nine 25
830 eight hundred and thirty 21
831 eight hundred and thirty-one 24
832 eight hundred and thirty-two 24
833 eight hundred and thirty-three 26
834 eight hundred and thirty-four 25
835 eight hundred and thirty-five 25
836 eight hundred and thirty-six 24
837 eight hundred and thirty-seven 26
838 eight hundred and thirty-eight 26
839 eight hundred and thirty-nine 25
840 eight hundred and forty 20
841 eight hundred and forty-one 23
842 eight hundred and forty-two 23
843 eight hundred and forty-three 25
844 eight hundred and forty-four 24
845 eight hundred and forty-five 24
846 eight hundred and forty-six 23
847 eight hundred and forty-seven 25
848 eight hundred and forty-eight 25
849 eight hundred and forty-nine 24
850 eight hundred and fifty 20
851 eight hundred and fifty-one 23
852 eight hundred and fifty-two 23
853 eight hundred and fifty-three 25
854 eight hundred and fifty-four 24
855 eight hundred and fifty-five 24
856 eight hundred and fifty-six 23
857 eight hundred and fifty-seven 25
858 eight hundred and fifty-eight 25
859 eight hundred and fifty-nine 24
860 eight hundred and sixty 20
861 eight hundred and sixty-one 23
862 eight hundred and sixty-two 23
863 eight hundred and sixty-three 25
864 eight hundred and sixty-four 24
865 eight hundred and sixty-five 24
866 eight hundred and sixty-six 23
867 eight hundred and sixty-seven 25
868 eight hundred and sixty-eight 25
869 eight hundred and sixty-nine 24
870 eight hundred and seventy 22
871 eight hundred and seventy-one 25
872 eight hundred and seventy-two 25
873 eight hundred and seventy-three 27
874 eight hundred and seventy-four 26
875 eight hundred and seventy-five 26
876 eight hundred and seventy-six 25
877 eight hundred and seventy-seven 27
878 eight hundred and seventy-eight 27
879 eight hundred and seventy-nine 26
880 eight hundred and eighty 21
881 eight hundred and eighty-one 24
882 eight hundred and eighty-two 24
883 eight hundred and eighty-three 26
884 eight hundred and eighty-four 25
885 eight hundred and eighty-five 25
886 eight hundred and eighty-six 24
887 eight hundred and eighty-seven 26
888 eight hundred and eighty-eight 26
889 eight hundred and eighty-nine 25
890 eight hundred and ninety 21
891 eight hundred and ninety-one 24
892 eight hundred and ninety-two 24
893 eight hundred and ninety-three 26
894 eight hundred and ninety-four 25
895 eight hundred and ninety-five 25
896 eight hundred and ninety-six 24
897 eight hundred and ninety-seven 26
898 eight hundred and ninety-eight 26
899 eight hundred and ninety-nine 25
900 nine hundred 11
901 nine hundred and one 17
902 nine hundred and two 17
903 nine hundred and three 19
904 nine hundred and four 18
905 nine hundred and five 18
906 nine hundred and six 17
907 nine hundred and seven 19
908 nine hundred and eight 19
909 nine hundred and nine 18
910 nine hundred and ten 17
911 nine hundred and eleven 20
912 nine hundred and twelve 20
913 nine hundred and thirteen 22
914 nine hundred and fourteen 22
915 nine hundred and fifteen 21
916 nine hundred and sixteen 21
917 nine hundred and seventeen 23
918 nine hundred and eighteen 22
919 nine hundred and nineteen 22
920 nine hundred and twenty 20
921 nine hundred and twenty-one 23
922 nine hundred and twenty-two 23
923 nine hundred and twenty-three 25
924 nine hundred and twenty-four 24
925 nine hundred and twenty-five 24
926 nine hundred and twenty-six 23
927 nine hundred and twenty-seven 25
928 nine hundred and twenty-eight 25
929 nine hundred and twenty-nine 24
930 nine hundred and thirty 20
931 nine hundred and thirty-one 23
932 nine hundred and thirty-two 23
933 nine hundred and thirty-three 25
934 nine hundred and thirty-four 24
935 nine hundred and thirty-five 24
936 nine hundred and thirty-six 23
937 nine hundred and thirty-seven 25
938 nine hundred and thirty-eight 25
939 nine hundred and thirty-nine 24
940 nine hundred and forty 19
941 nine hundred and forty-one 22
942 nine hundred and forty-two 22
943 nine hundred and forty-three 24
944 nine hundred and forty-four 23
945 nine hundred and forty-five 23
946 nine hundred and forty-six 22
947 nine hundred and forty-seven 24
948 nine hundred and forty-eight 24
949 nine hundred and forty-nine 23
950 nine hundred and fifty 19
951 nine hundred and fifty-one 22
952 nine hundred and fifty-two 22
953 nine hundred and fifty-three 24
954 nine hundred and fifty-four 23
955 nine hundred and fifty-five 23
956 nine hundred and fifty-six 22
957 nine hundred and fifty-seven 24
958 nine hundred and fifty-eight 24
959 nine hundred and fifty-nine 23
960 nine hundred and sixty 19
961 nine hundred and sixty-one 22
962 nine hundred and sixty-two 22
963 nine hundred and sixty-three 24
964 nine hundred and sixty-four 23
965 nine hundred and sixty-five 23
966 nine hundred and sixty-six 22
967 nine hundred and sixty-seven 24
968 nine hundred and sixty-eight 24
969 nine hundred and sixty-nine 23
970 nine hundred and seventy 21
971 nine hundred and seventy-one 24
972 nine hundred and seventy-two 24
973 nine hundred and seventy-three 26
974 nine hundred and seventy-four 25
975 nine hundred and seventy-five 25
976 nine hundred and seventy-six 24
977 nine hundred and seventy-seven 26
978 nine hundred and seventy-eight 26
979 nine hundred and seventy-nine 25
980 nine hundred and eighty 20
981 nine hundred and eighty-one 23
982 nine hundred and eighty-two 23
983 nine hundred and eighty-three 25
984 nine hundred and eighty-four 24
985 nine hundred and eighty-five 24
986 nine hundred and eighty-six 23
987 nine hundred and eighty-seven 25
988 nine hundred and eighty-eight 25
989 nine hundred and eighty-nine 24
990 nine hundred and ninety 20
991 nine hundred and ninety-one 23
992 nine hundred and ninety-two 23
993 nine hundred and ninety-three 25
994 nine hundred and ninety-four 24
995 nine hundred and ninety-five 24
996 nine hundred and ninety-six 23
997 nine hundred and ninety-seven 25
998 nine hundred and ninety-eight 25
999 nine hundred and ninety-nine 24
1000 one thousand 11

total letters =  21124

time= 0.12600016593933105
