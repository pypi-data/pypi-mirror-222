use pyo3::prelude::*;
use numpy::{IntoPyArray,
            PyArray2};

/// Formats the sum of two numbers as string.
#[pyfunction]
fn sum_as_string(a: usize, b: usize) -> PyResult<String> {
    Ok((a + b).to_string())
}

#[pyclass(module = "del_cad")]
struct MyClass{
    cad: del_cad::cad2::Cad2
}

#[pymethods]
impl MyClass {
    #[new]
    fn new() -> Self {
        Self {
            cad: del_cad::cad2::Cad2::new()
        }
    }

    fn add_polygon<'py>(
        &mut self,
        _py: Python<'py>,
        pos: Vec<f64>) {
        self.cad.add_polygon(&pos);
    }

    fn triangulation<'py>(
        &self,
        _py: Python<'py>,
        edge_length: f64)  -> (&'py PyArray2<usize>,
                               &'py PyArray2<f64>) {


        let mut mesher = del_cad::mesher_cad2::MesherCad2::new();
        mesher.edge_length = edge_length;
        let mesh = mesher.meshing(
            &self.cad);
        let (tri2vtx, vtx2xy) = del_dtri::array_from_2d_dynamic_triangle_mesh(
            &mesh.0, &mesh.2);
        (
            numpy::ndarray::Array2::from_shape_vec(
                (tri2vtx.len()/3,3), tri2vtx).unwrap().into_pyarray(_py),
            numpy::ndarray::Array2::from_shape_vec(
                (vtx2xy.len()/2,2), vtx2xy).unwrap().into_pyarray(_py)
        )
    }

    #[getter]
    fn get_num_vertex(&self) -> PyResult<usize>{
        Ok(self.cad.vertices.len())
    }


}


/// A Python module implemented in Rust.
#[pymodule]
fn del_cad(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(sum_as_string, m)?)?;
    m.add_class::<MyClass>()?;
    Ok(())
}

