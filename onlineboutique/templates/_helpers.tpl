{{/*
Chart Name
*/}}
{{- define "online-boutique.name" -}}
{{ .Chart.Name }}
{{- end }}

{{/*
Full Name
*/}}
{{- define "online-boutique.fullname" -}}
{{ .Release.Name }}
{{- end }}

{{/*
Namespace
*/}}
{{- define "online-boutique.namespace" -}}
{{ .Values.namespace }}
{{- end }}

{{/*
Frontend Service
*/}}
{{- define "online-boutique.frontend.service" -}}
frontend
{{- end }}

{{/*
Common Labels
*/}}
{{- define "online-boutique.labels" -}}
app.kubernetes.io/name: {{ include "online-boutique.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end }}