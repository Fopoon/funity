using System;
using System.IO;
using System.Linq;
using UnityEditor;
using UnityEditor.Build.Reporting;
using static funity.Utils;

namespace funity
{
    public class PlayerBuilder : IPlayerBuilder
    {
        public string Name { get; set; }

        public BuildTarget Target { get; set; }

        public bool Build()
        {
            var target = Target;
            var path = GetBuildPath(target);
            var scenes = GetScenes();

            var report = BuildPipeline.BuildPlayer(scenes, path, target, GetBuildOptions());

            return report != null && report.summary.result == BuildResult.Succeeded;
        }

        protected virtual string GetBuildFileExtension(BuildTarget buildTarget)
        {
            switch (buildTarget)
            {
                case BuildTarget.StandaloneOSX:
                    return ".app";
                case BuildTarget.StandaloneWindows:
                case BuildTarget.StandaloneWindows64:
                    return ".exe";
                case BuildTarget.iOS:
                    return null;
                case BuildTarget.Android:
                    return ".apk";
                case BuildTarget.WebGL:
                    break;
                case BuildTarget.WSAPlayer:
                    break;
                case BuildTarget.StandaloneLinux64:
                    return ".x64";
                case BuildTarget.PS4:
                    break;
                case BuildTarget.XboxOne:
                    break;
                case BuildTarget.tvOS:
                    break;
                case BuildTarget.Switch:
                    break;
                case BuildTarget.Lumin:
                    break;
                case BuildTarget.BJM:
                    break;
                case BuildTarget.NoTarget:
                    return null;
                default:
                    throw new ArgumentOutOfRangeException(nameof(buildTarget), buildTarget, null);
            }

            return null;
        }

        protected virtual string GetBuildFolder(BuildTarget buildTarget)
        {
            switch (buildTarget)
            {
                case BuildTarget.StandaloneOSX:
                    return "OSX";
                case BuildTarget.StandaloneWindows:
                case BuildTarget.StandaloneWindows64:
                    return "Windows";
                case BuildTarget.iOS:
                    return "iOS-XCode";
                case BuildTarget.Android:
                    return "Android";
                case BuildTarget.WebGL:
                    return "WebGL";
                case BuildTarget.WSAPlayer:
                    return "WSA";
                case BuildTarget.StandaloneLinux64:
                    return "Linux";
                case BuildTarget.PS4:
                    return "PS4";
                case BuildTarget.XboxOne:
                    return "XboxOne";
                case BuildTarget.tvOS:
                    return "tvOS";
                case BuildTarget.Switch:
                    return "Switch";
                case BuildTarget.Lumin:
                    return "Lumin";
                case BuildTarget.BJM:
                    return "BJM";
                case BuildTarget.NoTarget:
                    return null;
                default:
                    throw new ArgumentOutOfRangeException(nameof(buildTarget), buildTarget, null);
            }
        }

        protected virtual BuildOptions GetBuildOptions()
        {
            return BuildOptions.None;
        }

        protected virtual string GetBuildPath(BuildTarget target)
        {
            var buildPath = Path.Combine(GetBuildFolder(target), $"{Name}{GetBuildFileExtension(target)}");

            if (string.IsNullOrWhiteSpace(buildPath))
                throw new Exception("Unable to get the build path.");

            buildPath = Path.Combine("Builds", buildPath);

            Log($"Output path set to {buildPath}");

            return buildPath;
        }

        protected virtual BuildTargetGroup GetBuildTargetGroup(BuildTarget buildTarget)
        {
            switch (buildTarget)
            {
                case BuildTarget.StandaloneOSX:
                case BuildTarget.StandaloneWindows:
                case BuildTarget.StandaloneWindows64:
                case BuildTarget.StandaloneLinux64:
                    return BuildTargetGroup.Standalone;
                case BuildTarget.iOS:
                    return BuildTargetGroup.iOS;
                case BuildTarget.Android:
                    return BuildTargetGroup.Android;
                case BuildTarget.WebGL:
                    return BuildTargetGroup.WebGL;
                case BuildTarget.WSAPlayer:
                    return BuildTargetGroup.WSA;
                case BuildTarget.PS4:
                    return BuildTargetGroup.PS4;
                case BuildTarget.XboxOne:
                    return BuildTargetGroup.XboxOne;
                case BuildTarget.tvOS:
                    return BuildTargetGroup.tvOS;
                case BuildTarget.Switch:
                    return BuildTargetGroup.Switch;
                case BuildTarget.Lumin:
                    return BuildTargetGroup.Lumin;
                case BuildTarget.BJM:
                    return BuildTargetGroup.BJM;
                case BuildTarget.NoTarget:
                    return BuildTargetGroup.Unknown;
                default:
                    throw new ArgumentOutOfRangeException(nameof(buildTarget), buildTarget, null);
            }
        }

        protected virtual string[] GetScenes()
        {
            var scenes = EditorBuildSettings.scenes
                                            .Where(scene => scene.enabled && !string.IsNullOrWhiteSpace(scene.path))
                                            .Select(scene => scene.path)
                                            .ToArray();

            if (scenes == null || scenes.Length == 0)
                throw new Exception("Found no scenes to include in the build.");

            Log($"Found {scenes.Length} scenes.");
            for (var i = 0; i < scenes.Length; i++)
            {
                var scene = scenes[i];
                Log($"- [{i}] {Path.GetFileName(scene)?.PadRight(100)} ({scene})");
            }

            return scenes;
        }
    }
}