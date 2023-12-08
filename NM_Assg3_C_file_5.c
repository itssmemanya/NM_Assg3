#include<stdio.h>
#include<gsl/gsl_multimin.h>

// Defining Rosenbrock function
double rosenbrock(const gsl_vector *v) 
{
    double x,y;
    x = gsl_vector_get(v, 0);
    y = gsl_vector_get(v, 1);

    return (1 - x) * (1 - x) + 100 * (y - x*x) * (y - x*x);
}

int main() 
{
    const gsl_multimin_fminimizer_type *T;
    gsl_multimin_fminimizer *s;
    gsl_vector *x, *h;
    gsl_multimin_function function;
    int status;
    size_t i = 0;
    double size;
    h = gsl_vector_alloc(2);
    gsl_vector_set(h, 0, 0.01);
    gsl_vector_set(h, 1, 0.01);
  
    // Initial guess
    x = gsl_vector_alloc(2);
    gsl_vector_set(x, 0, 1.0);
    gsl_vector_set(x, 1, 0.0);

    // Function to minimize
    function.n = 2;
    function.f = rosenbrock;
    function.params = NULL;
    T = gsl_multimin_fminimizer_nmsimplex2;
    s = gsl_multimin_fminimizer_alloc(T, 2);
    gsl_multimin_fminimizer_set(s, &function, x, h);

    // Iterations
    do 
    {
        i++;
        status = gsl_multimin_fminimizer_iterate(s);

        if (status)
            break;

        size = gsl_multimin_fminimizer_size(s);
        status = gsl_multimin_test_size(size, 1e-4);

        if (status == GSL_SUCCESS) {
            printf(" Converged to minimum at iteration %zu\n", i);
        }

        printf(" Iteration %zu: x = %f, y = %f, f(x, y) = %f\n", i,
               gsl_vector_get(s->x, 0), gsl_vector_get(s->x, 1),
               s->fval);
    } while (status == GSL_CONTINUE && i < 100);

    // Freeing allocated memory
    gsl_vector_free(x);
    gsl_vector_free(h);
    gsl_multimin_fminimizer_free(s);

    return 0;
}