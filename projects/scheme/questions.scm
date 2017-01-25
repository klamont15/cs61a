(define (caar x) (car (car x)))
(define (cadr x) (car (cdr x)))
(define (cdar x) (cdr (car x)))
(define (cddr x) (cdr (cdr x)))

; Some utility functions that you may find useful to implement.
(define (map proc items)
  (if (null? items) nil
  (cons (proc (car items)) (map proc (cdr items)))
)
)

(define (filter predicate sequence)
  (cond ((null? sequence) nil)
        ((predicate (car sequence))
         (cons (car sequence)
               (filter predicate (cdr sequence))))
        (else (filter predicate (cdr sequence)))))

(define (cons-all first rests)
  (if (null? rests)
    nil
    (cons (cons first (car rests)) (cons-all first (cdr rests)))
  )
)

(define (combine l1 l2)
  (cond
    ((or (null? l1)(null? (car l1))) l2)
    ((or (null? l2) (null? (car l2))) l1)
    (else (cons (car l1) (combine (cdr l1) l2)))
  )
)

(define (zip pairs)
  (if (null? pairs) (cons nil nil)
  (cons (map car pairs) (cons (map cdr pairs) nil))
  )
)


;; Problem 17
;; Returns a list of two-element lists
(define (enumerate s)
  (define (index s ind)
    (if (null? s)
    nil
    (cons (cons ind (cons (car s) nil)) (index (cdr s) (+ ind 1)))
    )
  )
  (index s 0)
)

  ; END PROBLEM 17

;; Problem 18
;; List all ways to make change for TOTAL with DENOMS
(define (list-change total denoms)
  (cond
    ((or (null? denoms) (> 1 total)) (cons nil nil))
    ((> (car denoms) total) (list-change total (cdr denoms)))
    (else (combine (cons-all (car denoms) (list-change (- total (car denoms)) denoms)) (list-change total (cdr denoms))))
  )
)





;; Problem 19
;; Returns a function that checks if an expression is the special form FORM
(define (check-special form)
  (lambda (expr) (equal? form (car expr))))

(define lambda? (check-special 'lambda))
(define define? (check-special 'define))
(define quoted? (check-special 'quote))
(define let?    (check-special 'let))

;; Converts all let special forms in EXPR into equivalent forms using lambda
(define (let-to-lambda expr)
  (cond
    ((atom? expr) expr)
    ((quoted? expr) expr)
    ((or (lambda? expr)
             (define? expr))
         (let ((form   (car expr))
               (params (cadr expr))
               (body   (cddr expr)))
          (cons form (cons params (map let-to-lambda body)))
           ))
        ((let? expr)
         (let ((values (cadr expr))
               (body   (cddr expr)))
           ; BEGIN PROBLEM 19
           (cons (cons (quote lambda) (cons (car (zip (let-to-lambda values))) (let-to-lambda body))) (let-to-lambda (map car (cadr (zip values)))))

           ; END PROBLEM 19
           ))
        (else
         ; BEGIN PROBLEM 19
         (map let-to-lambda expr)
         ; END PROBLEM 19
         )))
