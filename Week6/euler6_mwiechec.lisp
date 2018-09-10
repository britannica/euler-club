(defun square (x) (* x x))

(defun sumrange (n)
  (if (= n 1)
      1
    (+ n (sumrange (- n 1)))))
    
(defun sumsqrange (n)
  (if (= n 1)
      1
    (+ (square n) (sumsqrange (- n 1)))))    

(write (- (square(sumrange 100)) (sumsqrange 100)))
