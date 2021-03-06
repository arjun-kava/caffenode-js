#ifndef CAFFE_NODEJS_BLOB_H_
#define CAFFE_NODEJS_BLOB_H_
#define CPU_ONLY 1

#include <node_api.h>
#include <caffe/caffe.hpp>
#include <string>
#include <vector>

#include "shared.h"

namespace caffenodejs {

class CaffeNode_Blob {
 public:
  static napi_status Init(napi_env env);
  static void Destructor(napi_env env, void* nativeObject, void* finalize_hint);
  static napi_status NewInstance(napi_env env, size_t argc, napi_value args[],
                                 napi_value* instance);
  static napi_value Reshape(napi_env env, napi_callback_info info);
  static napi_value ReshapeLike(napi_env env, napi_callback_info info);
  static napi_value shape(napi_env env, napi_callback_info info);
  static napi_value shape_string(napi_env env, napi_callback_info info);
  static napi_value num_axes(napi_env env, napi_callback_info info);
  static napi_value count(napi_env env, napi_callback_info info);
  static napi_value CanonicalAxisIndex(napi_env env, napi_callback_info info);
  static napi_value num(napi_env env, napi_callback_info info);
  static napi_value channels(napi_env env, napi_callback_info info);
  static napi_value height(napi_env env, napi_callback_info info);
  static napi_value width(napi_env env, napi_callback_info info);
 private:
  explicit CaffeNode_Blob(const int num, const int channels, const int height,
                          const int width);
  explicit CaffeNode_Blob(std::vector<int> &shape);
  ~CaffeNode_Blob();

  static napi_ref constructor;
  static napi_value New(napi_env env, napi_callback_info info);

  caffe::Blob<Dtype>* blob_;
  napi_env env_;
  napi_ref wrapper_;
};
}  // namespace caffenodejs

#endif  // CAFFE_NODEJS_BLOB_H_
