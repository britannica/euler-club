;;; common lisp solution to Euler Week 6
(defun square (x) (* x x))

;;; recursive loop from n to 1 summing as you come back
(defun sumrange (n)
  (if (= n 1)
      1
    (+ n (sumrange (- n 1)))
  )
)

;;; recursive loop from n to 1 summing squares    
(defun sumsqrange (n)
  (if (= n 1)
      1
    (+ (square n) (sumsqrange (- n 1)))
  )
)    

(write (- (square(sumrange 100)) (sumsqrange 100)))
