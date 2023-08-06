#![feature(test)]



use pyo3::prelude::*;

/// Formats the sum of two numbers as string.
#[pyfunction]
fn sum_as_string(a: usize, b: usize) -> PyResult<String> {
    Ok((a + b).to_string())
}

/// A Python module implemented in Rust.
#[pymodule]
fn opti_solve(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(sum_as_string, m)?)?;
    Ok(())
}




#[cfg(test)]
mod tests {
    extern crate test;
    use test::Bencher;

    #[test]
    fn test(){

    }
    // #[bench]
    // fn bencher(b: &mut Bencher) {
    //     use std::mem::size_of_val;
    //     struct Zero;
    //     struct One;
    //     static ZERO: Zero = Zero;
    //     static ONE: One = One;
    //
    //     let (zero, one) = unsafe { (&ZERO as *const Zero as usize, &ONE as *const One as usize) };
    //
    //     println!(
    //         "{}\n{}\n{}\n{}\n{}",
    //         zero,
    //         one,
    //         one as isize - zero as isize,
    //         size_of_val(&ZERO),
    //         size_of_val(&ONE)
    //     );
    //
    //     let v = vec![7u128; 100000];
    //     b.iter(|| v.iter().sum::<u128>());
    // }
}