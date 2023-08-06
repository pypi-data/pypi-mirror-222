use pyo3::prelude::*;

use sqlformat;

#[pyfunction]
// allow a sql query, query params, and options
fn fmt_sql(sql_query: &str) -> PyResult<String> {
    let formatted_sql = sqlformat::format(
        sql_query,
        &sqlformat::QueryParams::default(),
        sqlformat::FormatOptions::default(),
    );
    Ok(formatted_sql)
}

/// A Python module implemented in Rust.
#[pymodule]
fn dizz(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(fmt_sql, m)?)?;
    Ok(())
}
