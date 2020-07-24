using JetBrains.Annotations;
using UnityEditor;
using static funity.Utils;

namespace funity
{
    public static class SetSerializationMode
    {
        [UsedImplicitly]
        public static void ForceBinary()
        {
            Set(SerializationMode.ForceBinary);
        }

        [UsedImplicitly]
        public static void ForceText()
        {
            Set(SerializationMode.ForceText);
        }

        [UsedImplicitly]
        public static void Mixed()
        {
            Set(SerializationMode.Mixed);
        }

        private static void Set(SerializationMode serializationMode)
        {
            Log($"{nameof(SetSerializationMode)}.{serializationMode}");

            EditorSettings.serializationMode = serializationMode;

            Quit(EditorSettings.serializationMode == serializationMode);
        }
    }
}