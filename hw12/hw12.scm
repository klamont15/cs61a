(define (find s predicate)
  (cond
    ((null? s) False)
    ((predicate (car s)) (car s))
    (else (find (cdr-stream s) predicate))
  )
)

(define (scale-stream s k)
  (if (null? s) nil
  (cons-stream (* k (car s)) (scale-stream (cdr-stream s) k))
  )
)

(define (has-cycle s)
  (define (helper-function t storage)
    (cond
      ((null? storage) False)
      ((eq? t storage) True)
      (else (helper-function t (cdr-stream storage)))
    )
  )
  (helper-function s (cdr-stream s))
)
(define (has-cycle-constant s)
  'YOUR-CODE-HERE
)
