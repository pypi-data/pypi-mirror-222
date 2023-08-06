#include "Mattress.h"
#include <string>
#include <stdexcept>
#include <cstring>
#include <cstdint>

template<typename Data_, typename Index_>
Mattress* initialize_compressed_sparse_matrix(int nr, int nc, uint64_t nz, const Data_* dptr, const Index_* iptr, void* indptr, uint8_t byrow) { 
    tatami::ArrayView<Data_> dview(dptr, nz);
    tatami::ArrayView<Index_> iview(iptr, nz);
    tatami::ArrayView<uint64_t> pview(reinterpret_cast<uint64_t*>(indptr), (byrow ? nr : nc) + 1);

    // Disabling checks for speed.
    if (byrow) {
        return new Mattress(new tatami::CompressedSparseRowMatrix<double, int, decltype(dview), decltype(iview), decltype(pview)>(nr, nc, std::move(dview), std::move(iview), std::move(pview), false));
    } else {
        return new Mattress(new tatami::CompressedSparseColumnMatrix<double, int, decltype(dview), decltype(iview), decltype(pview)>(nr, nc, std::move(dview), std::move(iview), std::move(pview), false));
    }
}

template<typename Data_>
Mattress* initialize_compressed_sparse_matrix_itype(int nr, int nc, uint64_t nz, const Data_* dptr, const char* itype, void* iptr, void* indptr, uint8_t byrow) {
    if (std::strcmp(itype, "int64") == 0) {
        return initialize_compressed_sparse_matrix(nr, nc, nz, dptr, reinterpret_cast< int64_t*>(iptr), indptr, byrow);

    } else if (std::strcmp(itype, "int32") == 0) {
        return initialize_compressed_sparse_matrix(nr, nc, nz, dptr, reinterpret_cast< int32_t*>(iptr), indptr, byrow);

    } else if (std::strcmp(itype, "int16") == 0) {
        return initialize_compressed_sparse_matrix(nr, nc, nz, dptr, reinterpret_cast< int16_t*>(iptr), indptr, byrow);

    } else if (std::strcmp(itype, "int8") == 0) {
        return initialize_compressed_sparse_matrix(nr, nc, nz, dptr, reinterpret_cast<  int8_t*>(iptr), indptr, byrow);

    } else if (std::strcmp(itype, "uint64") == 0) {
        return initialize_compressed_sparse_matrix(nr, nc, nz, dptr, reinterpret_cast<uint64_t*>(iptr), indptr, byrow);

    } else if (std::strcmp(itype, "uint32") == 0) {
        return initialize_compressed_sparse_matrix(nr, nc, nz, dptr, reinterpret_cast<uint32_t*>(iptr), indptr, byrow);

    } else if (std::strcmp(itype, "uint16") == 0) {
        return initialize_compressed_sparse_matrix(nr, nc, nz, dptr, reinterpret_cast<uint16_t*>(iptr), indptr, byrow);

    } else if (std::strcmp(itype, "uint8") == 0) {
        return initialize_compressed_sparse_matrix(nr, nc, nz, dptr, reinterpret_cast< uint8_t*>(iptr), indptr, byrow);
    }

    throw std::runtime_error("unrecognized type '" + std::string(itype) + "' for sparse matrix indices");
    return NULL;
}

extern "C" {

Mattress* py_initialize_compressed_sparse_matrix(int nr, int nc, uint64_t nz, const char* dtype, void* dptr, const char* itype, void* iptr, void* indptr, uint8_t byrow) {
    if (std::strcmp(dtype, "float64") == 0) {
        return initialize_compressed_sparse_matrix_itype(nr, nc, nz, reinterpret_cast<  double*>(dptr), itype, iptr, indptr, byrow);

    } else if (std::strcmp(dtype, "float32") == 0) {
        return initialize_compressed_sparse_matrix_itype(nr, nc, nz, reinterpret_cast<   float*>(dptr), itype, iptr, indptr, byrow);

    } else if (std::strcmp(dtype, "int64") == 0) {
        return initialize_compressed_sparse_matrix_itype(nr, nc, nz, reinterpret_cast< int64_t*>(dptr), itype, iptr, indptr, byrow);

    } else if (std::strcmp(dtype, "int32") == 0) {
        return initialize_compressed_sparse_matrix_itype(nr, nc, nz, reinterpret_cast< int32_t*>(dptr), itype, iptr, indptr, byrow);

    } else if (std::strcmp(dtype, "int16") == 0) {
        return initialize_compressed_sparse_matrix_itype(nr, nc, nz, reinterpret_cast< int16_t*>(dptr), itype, iptr, indptr, byrow);

    } else if (std::strcmp(dtype, "int8") == 0) {
        return initialize_compressed_sparse_matrix_itype(nr, nc, nz, reinterpret_cast<  int8_t*>(dptr), itype, iptr, indptr, byrow);

    } else if (std::strcmp(dtype, "uint64") == 0) {
        return initialize_compressed_sparse_matrix_itype(nr, nc, nz, reinterpret_cast<uint64_t*>(dptr), itype, iptr, indptr, byrow);

    } else if (std::strcmp(dtype, "uint32") == 0) {
        return initialize_compressed_sparse_matrix_itype(nr, nc, nz, reinterpret_cast<uint32_t*>(dptr), itype, iptr, indptr, byrow);

    } else if (std::strcmp(dtype, "uint16") == 0) {
        return initialize_compressed_sparse_matrix_itype(nr, nc, nz, reinterpret_cast<uint16_t*>(dptr), itype, iptr, indptr, byrow);

    } else if (std::strcmp(dtype, "uint8") == 0) {
        return initialize_compressed_sparse_matrix_itype(nr, nc, nz, reinterpret_cast< uint8_t*>(dptr), itype, iptr, indptr, byrow);
    }

    throw std::runtime_error("unrecognized array type '" + std::string(dtype) + "' for sparse matrix data");
    return NULL;
}

}

