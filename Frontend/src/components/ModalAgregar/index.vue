<template>
  <el-dialog
    v-el-drag-dialog
    :visible.sync="modalvisible"
    :before-close="handleCancel"
    :width="x.matches ? '' : '40%'"
    :fullscreen="x.matches ? true : false"
    custom-class="dialog-class"
    :show-close="true"
    :destroy-on-close="true"
    :close-on-click-modal="true"
    :close-on-press-escape="true"
    append-to-body
  >
    <sticky class-name="sub-navbar">
      <div style="border: 0px solid red; color: white; text-align: center">
        <h2>{{ modaltitulo }}</h2>
      </div>
    </sticky>
    <div
      class="createPost-container"
      style="padding-top: 20px; padding-bottom: 20px; padding-left: 13px"
    >
      <el-form
        ref="modalform"
        :model="model"
        :rules="rulesform"
        label-width="160px"
        :label-position="x.matches ? 'top' : ''"
        class="demo-ruleForm"
      >
        <el-form-item v-for="component in domcomponents" :key="component.prop" :label="component.label" :prop="component.prop">
          <span v-if="component.type === 'buttonInput'">
            <div style="padding-left: 15%;">
              <b>{{ component.text }}</b>&nbsp;&nbsp;<el-button type="success" size="medium" icon="el-icon-plus" circle @click="handleAddInput" />
            </div>
          </span>
          <span v-if="component.type === 'divider'">
            <div style="border-top: 1px solid #C0C4CC; width: 86%;" />
          </span>
          <span v-if="component.type === 'radiogroup'">
            <el-radio-group v-model="model[component.prop]">
              <el-radio-button
                v-for="item in datamodal[component.prop]"
                :key="item.id"
                :label="item.label"
              />
            </el-radio-group>
          </span>
          <span v-if="component.type === 'text'">
            <el-input
              v-model="model[component.prop]"
              autocomplete="off"
              :placeholder="component.placeholder"
              :maxlength="component.maxlength"
              :show-word-limit="component.showwordlimit"
              class="control-modal"
              @keyup.enter.native="handleForm('modalform')"
            />
          </span>
          <span v-if="component.type === 'email'">
            <el-input
              v-model="model[component.prop]"
              autocomplete="off"
              :placeholder="component.placeholder"
              clearable
              :class="component.show ? 'control-modal-small' : 'control-modal'"
              @keyup.enter.native="handleForm('modalform')"
            />
            <el-button v-show="component.show" type="danger" size="mini" icon="el-icon-minus" circle @click="removeInput(component)" />
          </span>
          <span v-if="component.type === 'number'">
            <el-input
              v-model.number="model[component.prop]"
              autocomplete="off"
              class="control-modal"
              :placeholder="component.placeholder"
              @keyup.enter.native="handleForm('modalform')"
            />
          </span>
          <span v-if="component.type === 'decimal'">
            <el-input-number
              v-model.number="model[component.prop]"
              :precision="2"
              :step="0.01"
              autocomplete="off"
              class="control-modal"
              :placeholder="component.placeholder"
              @keyup.enter.native="handleForm('modalform')"
            />
          </span>
          <span v-if="component.type === 'datetime'">
            <el-date-picker
              v-model="model[component.prop]"
              type="datetime"
              :placeholder="component.placeholder"
              class="control-modal"
            />
          </span>
          <span v-if="component.type === 'date'">
            <el-date-picker
              v-model="model[component.prop]"
              type="date"
              :placeholder="component.placeholder"
              class="control-modal"
            />
          </span>
          <span v-if="component.type === 'textarea'">
            <el-input
              v-model="model[component.prop]"
              type="textarea"
              class="control-modal"
              rows="4"
              :placeholder="component.placeholder"
            />
          </span>
          <span v-if="component.type === 'select'">
            <el-select
              v-model="model[component.prop]"
              filterable
              :placeholder="component.placeholder"
              class="control-modal"
              clearable
              :disabled="component.disabled"
            >
              <span>
                <el-option
                  v-for="item in datamodal[component.prop]"
                  :key="item.id"
                  :label="item.nombre"
                  :value="item.id"
                />
              </span>
            </el-select>
          </span>
        </el-form-item>
        <el-form-item>
          <el-button @click="handleCancel()">Cancelar</el-button>
          <el-button
            type="success"
            @click="handleForm('modalform')"
          >{{ action }}</el-button>
        </el-form-item>
      </el-form>
    </div>
  </el-dialog>
</template>

<script>
import elDragDialog from '@/directive/el-drag-dialog' // base on element-ui
import Sticky from '@/components/Sticky' // 粘性header组件
import moment from 'moment'

export default {
  name: 'ModalConfirm',
  directives: { elDragDialog },
  components: { Sticky },
  props: {
    modalvisible: {
      type: Boolean,
      default: false
    },
    modaltitulo: {
      type: String,
      default: ''
    },
    modalform: {
      type: Object,
      default: null
    },
    domcomponents: {
      type: Array,
      default: null
    },
    rulesform: {
      type: Object,
      default: null
    },
    datamodal: {
      type: Object,
      default: null
    },
    action: {
      type: String,
      default: ''
    }
  },
  data() {
    return {
      model: {},
      x: ''
    }
  },
  watch: {
    modalform: {
      deep: true,
      handler(val) {
        // console.log('Modelo agregar -> ', val)
        this.model = val
      }
    }
  },
  created() {
    this.model = {}
    this.x = window.matchMedia('(max-width: 800px)')
  },
  methods: {
    handleAddInput() {
      const propInput = `email${moment().unix()}${Math.floor(Math.random() * (10000 - 1)) + 1}`
      const input = {
        type: 'email',
        prop: propInput,
        // label: 'correo1',
        placeholder: 'Ingrese un correo',
        show: true
      }
      this.domcomponents.push(input)
      this.rulesform[propInput] = [{ type: 'email', required: true, message: 'Ingrese un correo electrónico válido', trigger: 'blur' }]
    },
    removeInput(component) {
      const posInput = this.domcomponents.indexOf(component)
      this.domcomponents.splice(posInput, 1)
      delete this.model[component.prop] // Eliminamos el input del modelo
      delete this.rulesform[component.prop] // Eliminamos la regla del input
    },
    async handleForm(formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          // Devolvemos el object del form y cerramos el dialogo
          // console.log('MODELO -> ', this.modalform)
          this.$emit('confirmar', { response: true, action: this.action, data: this.model })
        } else {
          console.log('error submit!!')
          return false
        }
      })
    },
    handleCancel() {
      // console.log(this.action)
      if (this.action === 'Agregar') { // Se deja a solo agregar ya que cuando es editar se daña el formulario
        this.$refs['modalform'].resetFields()
      }
      this.$emit('confirmar', { response: false })
    }
  }
}
</script>

<style lang="scss" scoped>

// Pantallas superiores a 800px (PC)
@media screen and (min-width: 800px) {
  .control-modal {
    width: 85%;
  }

  .control-modal-small {
    width: 75%;
  }
}

// Pantallas inferiores a 800px (mobile)
@media screen and (max-width: 800px) {
  .control-modal {
    width: 95%;
  }

  .control-modal-small {
    width: 85%;
  }
}
</style>

<style lang="scss">

// Pantallas superiores a 800px (PC)
@media screen and (min-width: 800px) {
  .dialog-class {
    border-radius: 10px;
  }

  .dialog-class .el-dialog__body {
    padding-top: 0 !important;
  }
}

// Pantallas inferiores a 800px (mobile)
@media screen and (max-width: 800px) {
  .dialog-class .el-dialog__body {
    padding: 0 !important;
  }

  .dialog-class .el-dialog__header {
    display: none;
  }
}
</style>
